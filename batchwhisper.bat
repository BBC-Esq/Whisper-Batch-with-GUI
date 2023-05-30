@echo off

setlocal enabledelayedexpansion

set "model=%~1"
set "include_subdirs_from_gui=%~2"
set "output_format=%~3"
set "translate_from_gui=%~4"
set "selected_language=%~5"
echo Debug: Model: %model%
echo Debug: Include Subdirs: %include_subdirs_from_gui%
echo Debug: Output Format: %output_format%
echo Debug: Translate: %translate_from_gui%
echo Debug: Selected Language: %selected_language%

echo Checking if Whisper is installed...
where "whisper.exe" >nul
if not errorlevel 1 (
    echo Whisper is installed.
) else (
    echo "Unable to run. Whisper might not be installed, in the system PATH, the user does not have sufficient permissions to access the file system, or another reason. Exiting..."
    pause >nul
    exit /b 1
)

if /i "%include_subdirs_from_gui%"=="1" (
    set "include_subdirs=yes"
) else (
    set "include_subdirs=no"
)

set "log_error=false"

set /a "total_files=0"
set /a "processed_files=0"
set /a "skipped_files=0"

if /i "%include_subdirs%"=="yes" (
    for /R %%A in (*.mp3;*.wav;*.wma) do (
        set /a "total_files+=1"
    )
) else (
    for %%A in (*.mp3;*.wav;*.wma) do (
        if "%%~dpA"=="%CD%\" (
            set /a "total_files+=1"
        )
    )
)

if /i "%include_subdirs%"=="yes" (
    for /R %%A in (*.mp3;*.wav;*.wma) do (
        set "audio_file=%%A"
        call :process_file
    )
) else (
    for %%A in (*.mp3;*.wav;*.wma) do (
        set "audio_file=%%~fA"
        call :process_file
    )
)

if %log_error%==true (
    set "hour=%time:~0,2%"
    if "%hour:~0,1%"==" " set "hour=0%hour:~1,1%"
    set "log_file=log_%date:~10,4%%date:~4,2%%date:~7,2%_%hour%%time:~3,2%%time:~6,2%.txt"
    echo Script started: %date% %time% > "%log_file%"
    echo Total files: %total_files% >> "%log_file%"
    echo Skipped files: %skipped_files% >> "%log_file%"
    type "%log_file%" | findstr /C:"Error: Failed"
    echo There were errors during processing. Check the log file for details.
)

goto :eof

:process_file
set /a "processed_files+=1"
echo [%processed_files%/%total_files%] Processing file: "!audio_file!"

if /i "%translate_from_gui%"=="1" (
    set "translate_arg=--task translate"
    set "language_arg=--language %selected_language%"
) else (
    set "translate_arg="
    set "language_arg="
)

echo Running command: whisper "!audio_file!" --model !model! --output_format !output_format! !translate_arg! !language_arg!
whisper "!audio_file!" --model !model! --output_format !output_format! !translate_arg! !language_arg! 2> nul

if errorlevel 1 (
    echo Error: Failed to process "!audio_file!" using the whisper command.
    set /a "skipped_files+=1"
    set "log_error=true"
    goto :eof
) else (
    echo Successfully processed "!audio_file!".
)

if /i "!translate_from_gui!"=="1" (
    if not "!output_format!"=="srt" (
        echo Error: Translating is only supported for the srt output format. Skipping translation for "!audio_file!".
    ) else (
        set "language=!selected_language!"
        if "!language!"=="" (
            echo Error: No language selected for translation. Skipping translation for "!audio_file!".
        ) else (
            echo Translating subtitles for "!audio_file!" to language: "!language!"...
            python translate.py "!audio_file!.srt" "!language!" 2> nul
            if errorlevel 1 (
                echo Error: Failed to translate subtitles for "!audio_file!" to language: "!language!".
                set "log_error=true"
            ) else (
                echo Successfully translated subtitles for "!audio_file!" to language: "!language!".
            )
        )
    )
)

goto :eof