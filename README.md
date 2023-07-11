## Requirements:

- Python — Whisper — Pytorch — CUDA
- Tested with: Python 3.10 — CUDA 11.8 — Pytorch 2.0

## Instructions:

1. Put all three files anywhere that is in your system `PATH`.
2. Open a command prompt in the directory where your audio files are located.
3. Type "batchwhispermenu" and hit `ENTER`.

## Summary of Scripts:

| Script                  | Summary                                                                                                                                      |
|-------------------------|----------------------------------------------------------------------------------------------------------------------------------------------|
| batchwhispermenu.bat  | Initiates "batchwhispermenu.py"                                                                                                              |
| batchwhispermenu.py   | A GUI that allows a user to select a model, output format, source language, and whether to include subdirectories and translations.           |
| batchwhisper.bat      | Runs the Whisper program with the parameters selected in the GUI.                                                                             |

## ADDITIONAL RESOURCES:

There are two primary methods to significantlky speed up OpenAI's Whisper:

(1) - C++
- [https://github.com/ggerganov/whisper.cpp](https://github.com/ggerganov/whisper.cpp)
- [https://github.com/Const-me/Whisper](https://github.com/Const-me/Whisper)
- [https://github.com/aarnphm/whispercpp](https://github.com/aarnphm/whispercpp)
- [https://github.com/stlukey/whispercpp.py](https://github.com/stlukey/whispercpp.py)
- [https://github.com/tigros/Whisperer](https://github.com/tigros/Whisperer)

(2) - Ctranslate2
- [https://github.com/guillaumekln/faster-whisper](https://github.com/guillaumekln/faster-whisper)
- [https://github.com/Purfview/whisper-standalone-win](https://github.com/Purfview/whisper-standalone-win)
- [https://github.com/Softcatala/whisper-ctranslate2](https://github.com/Softcatala/whisper-ctranslate2)
- [https://github.com/m-bain/whisperX](https://github.com/m-bain/whisperX)
