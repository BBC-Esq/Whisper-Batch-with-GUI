## Requirements:

- Python — Whisper — Pytorch — CUDA

## Tested with:

- Python 3.10 — CUDA 11.8 — Pytorch 2.0

**Note: Please refer to the official documentation for instructions on how to install these technologies.**

## Instructions:

1. Put all three files anywhere that is in your system `PATH`.
2. Open a command prompt in the directory where your audio files are located.
3. Type "batchwhispermenu" and hit `ENTER`.

## Summary of Scripts:

| Script                  | Summary                                                                                                                                      |
|-------------------------|----------------------------------------------------------------------------------------------------------------------------------------------|
| "batchwhispermenu.bat"  | Initiates "batchwhispermenu.py"                                                                                                              |
| "batchwhispermenu.py"   | A GUI that allows a user to select a model, output format, source language, and whether to include subdirectories and translations.           |
| "batchwhisper.bat"      | Runs the Whisper program with the parameters selected in the GUI.                                                                             |

## TO-DO (feel free to submit a pull request):

I want to speed up Whisper by using some or all of the following great repos:

- [https://github.com/ggerganov/whisper.cpp](https://github.com/ggerganov/whisper.cpp)
- [https://github.com/sanchit-gandhi/whisper-jax](https://github.com/sanchit-gandhi/whisper-jax)
- [https://github.com/m-bain/whisperX](https://github.com/m-bain/whisperX)
- [https://github.com/guillaumekln/faster-whisper](https://github.com/guillaumekln/faster-whisper)

Links to repos that are more robust but not as lightweight as mine:

- [https://github.com/Const-me/Whisper](https://github.com/Const-me/Whisper)
- [https://github.com/tigros/Whisperer](https://github.com/tigros/Whisperer)

Feel free to explore these projects if you're looking for more robust alternatives.
