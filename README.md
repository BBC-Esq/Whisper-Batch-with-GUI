SCRIPT SUMMARIES:

"batchwhispermenu.py"
This script creates a GUI for a batch processing tool called "batchwhisper.bat". The GUI allows users to select a model, output format, source language, and whether to include subdirectories and translations. Upon hitting "Run", it launches "batchwhisper.bat" with the selected parameters in a separate thread. It also notifies users when the process completes and handles the case where "batchwhisper.bat" isn't found.

"batchwhispermenu.bat"
Initiates "batchwhispermenu.py"

"batchwhisper.bat"
This is the script that actually runs the Whisper command after receiving the options selected through the GUI.

TO USE:

Put all three files in the system path, open a command prompte IN THE DIRECTORY YOU WANT TO PROCESS FILES, type "batchwhispermenu" and hit Enter.  Thats it.

CLOSING ARGUMENT:
This is my first program ever and first Github repo ever.  Thanks for visiting.

 TO DO LIST IF ANYONE WANTS TO HELP:

*** Implement the technology if "ggml" models like at https://github.com/Const-me/Whisper.  Please contact me if you know how I might do this.

*** Include an option for transcribing live audio, again, like the above repo.  My hat's off to that guy.

*** Improve the GUI to allow you to select multiple files within a directory, not just "all files," just like https://github.com/tigros/Whisperer  

*** Once everything is finalized, create an installer/EXE so it's easier to run.
