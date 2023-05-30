import os
import subprocess
import shutil
from tkinter import *
from tkinter import ttk
from tkinter import filedialog


def run_batch_script():
    script_name = "batchwhisper.bat"

    script_path = shutil.which(script_name)
    if script_path is None:
        print("batchwhisper2.bat not found in the system path. Please check the system path configuration.")
        return

    selected_model = model_var.get() or ""
    include_subdirs = "1" if include_subdirs_var.get() == "True" else "0"
    selected_format = format_var.get() or ""
    translate = "1" if translate_var.get() else ""
    selected_language = language_var.get() or ""

    command = f"{script_path} {selected_model} {include_subdirs} {selected_format} {translate} {selected_language}"
    subprocess.run(command, shell=True)


def toggle_language_menu():
    if translate_var.get():
        language_menu.config(state="readonly")
    else:
        language_menu.config(state="disabled")


root = Tk()
root.title("Whisper GUI")

screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()

min_window_width = 400
root.minsize(min_window_width, -1)

root.update_idletasks()

window_width = root.winfo_width()
window_height = root.winfo_height()
window_height += 25  # Increase window height by 50 pixels
x_position = int((screen_width / 2) - (window_width / 2))
y_position = int((screen_height / 2) - (window_height / 2))

root.geometry(f'{window_width}x{window_height}+{x_position}+{y_position}')

frame = Frame(root)
frame.pack(padx=10, pady=10)

Label(frame, text="Choose the Whisper model:").grid(row=0, column=0, sticky=W)

model_var = StringVar()
model_var.set("large-v2")

model_options = [
    "tiny.en", "tiny", "base.en", "base", "small.en", "small",
    "medium.en", "medium", "large", "large-v1", "large-v2"
]

model_menu = ttk.Combobox(frame, textvariable=model_var, values=model_options, state="readonly", justify="left")
model_menu.grid(row=0, column=1, sticky=W)

Label(frame, text="Choose the output format:").grid(row=1, column=0, sticky=W)

format_var = StringVar()
format_var.set("vtt")

format_options = [
    "txt", "vtt", "srt", "tsv", "json", "all"
]

format_menu = ttk.Combobox(frame, textvariable=format_var, values=format_options, state="readonly", justify="left")
format_menu.grid(row=1, column=1, sticky=W)

include_subdirs_var = StringVar()
include_subdirs_var.set(False)

include_subdirs_checkbox = Checkbutton(
    frame,
    text="Include subdirectories",
    variable=include_subdirs_var,
    onvalue="True",
    offvalue="False",
    justify="left",
)
include_subdirs_var.set("False")
include_subdirs_checkbox.grid(row=2, columnspan=2, sticky=W)

translate_var = BooleanVar()
translate_var.set(False)

translate_checkbox = Checkbutton(frame, text="Translate to English", variable=translate_var, command=toggle_language_menu, justify="left")
translate_checkbox.grid(row=3, columnspan=2, sticky=W)

Label(frame, text="Choose the source language:").grid(row=4, column=0, sticky=W)

language_var = StringVar()

language_options = [
    "Afrikaans","Albanian","Amharic","Arabic","Armenian","Assamese","Azerbaijani","Bashkir","Basque","Belarusian",
    "Bengali","Bosnian","Breton","Bulgarian","Burmese","Castilian","Catalan","Chinese","Croatian","Czech",
    "Danish","Dutch","English","Estonian","Faroese","Finnish","Flemish","French","Galician","Georgian",
    "German","Greek","Gujarati","Haitian","Haitian Creole","Hausa","Hawaiian","Hebrew","Hindi","Hungarian",
    "Icelandic","Indonesian","Italian","Japanese","Javanese","Kannada","Kazakh","Khmer","Korean","Lao",
    "Latin","Latvian","Letzeburgesch","Lingala","Lithuanian","Luxembourgish","Macedonian","Malagasy","Malay",
    "Malayalam","Maltese","Maori","Marathi","Moldavian","Moldovan","Mongolian","Myanmar","Nepali","Norwegian",
    "Nynorsk","Occitan","Panjabi","Pashto","Persian","Polish","Portuguese","Punjabi","Pushto","Romanian","Russian",
    "Sanskrit","Serbian","Shona","Sindhi","Sinhala","Sinhalese","Slovak","Slovenian","Somali","Spanish","Sundanese",
    "Swahili","Swedish","Tagalog","Tajik","Tamil","Tatar","Telugu","Thai","Tibetan","Turkish","Turkmen","Ukrainian",
    "Urdu","Uzbek","Valencian","Vietnamese","Welsh","Yiddish","Yoruba"
]

language_menu = ttk.Combobox(frame, textvariable=language_var, values=language_options, state="disabled", justify="left")
language_menu.grid(row=4, column=1, sticky=W)

run_button = Button(frame, text="Run", command=run_batch_script)
run_button.grid(row=5, columnspan=2, pady=10)

toggle_language_menu()

root.mainloop()