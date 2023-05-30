import shutil
import sys
import subprocess
from PyQt6.QtCore import QThread
from PyQt6.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QCheckBox, QComboBox, QLabel, QPushButton, QWidget


class BatchProcessThread(QThread):
    def __init__(self, command):
        super().__init__()
        self.command = command

    def run(self):
        subprocess.run(self.command, shell=True)


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.model_combo = QComboBox()
        self.model_combo.addItems(["tiny.en", "tiny", "base.en", "base", "small.en", "small",
                                   "medium.en", "medium", "large", "large-v1", "large-v2"])

        self.format_combo = QComboBox()
        self.format_combo.addItems(["txt", "vtt", "srt", "tsv", "json", "all"])

        self.include_subdirs_checkbox = QCheckBox("Include subdirectories")
        self.translate_checkbox = QCheckBox("Translate to English")

        self.language_combo = QComboBox()
        self.language_combo.addItems([
            "Afrikaans", "Albanian", "Amharic", "Arabic", "Armenian", "Assamese", "Azerbaijani", "Bashkir", "Basque",
            "Belarusian", "Bengali", "Bosnian", "Breton", "Bulgarian", "Burmese", "Castilian", "Catalan", "Chinese",
            "Croatian", "Czech", "Danish", "Dutch", "English", "Estonian", "Faroese", "Finnish", "Flemish", "French",
            "Galician", "Georgian", "German", "Greek", "Gujarati", "Haitian", "Haitian Creole", "Hausa", "Hawaiian",
            "Hebrew", "Hindi", "Hungarian", "Icelandic", "Indonesian", "Italian", "Japanese", "Javanese", "Kannada",
            "Kazakh", "Khmer", "Korean", "Lao", "Latin", "Latvian", "Letzeburgesch", "Lingala", "Lithuanian",
            "Luxembourgish", "Macedonian", "Malagasy", "Malay", "Malayalam", "Maltese", "Maori", "Marathi", "Moldavian",
            "Moldovan", "Mongolian", "Myanmar", "Nepali", "Norwegian", "Nynorsk", "Occitan", "Panjabi", "Pashto",
            "Persian", "Polish", "Portuguese", "Punjabi", "Pushto", "Romanian", "Russian", "Sanskrit", "Serbian",
            "Shona", "Sindhi", "Sinhala", "Sinhalese", "Slovak", "Slovenian", "Somali", "Spanish", "Sundanese",
            "Swahili", "Swedish", "Tagalog", "Tajik", "Tamil", "Tatar", "Telugu", "Thai", "Tibetan", "Turkish",
            "Turkmen", "Ukrainian", "Urdu", "Uzbek", "Valencian", "Vietnamese", "Welsh", "Yiddish", "Yoruba"])

        self.run_button = QPushButton("Run")

        self.setup_ui()

    def setup_ui(self):
        self.setWindowTitle("Whisper GUI")
        layout = QVBoxLayout()

        widgets = [self.model_combo, self.format_combo, self.include_subdirs_checkbox, 
                   self.translate_checkbox, self.language_combo, self.run_button]
        labels = ["Choose the Whisper model:", "Choose the output format:", 
                  None, None, "Choose the source language:", None]

        for widget, label in zip(widgets, labels):
            if label:
                layout.addWidget(QLabel(label))
            layout.addWidget(widget)

        self.translate_checkbox.stateChanged.connect(self.toggle_language_menu)
        self.run_button.clicked.connect(self.run_batch_script)

        self.setCentralWidget(QWidget())
        self.centralWidget().setLayout(layout)
        self.toggle_language_menu()

    def toggle_language_menu(self):
        self.language_combo.setEnabled(self.translate_checkbox.isChecked())

    def run_batch_script(self):
        script_path = shutil.which("batchwhisper.bat")
        if not script_path:
            print("batchwhisper.bat not found in the system path. Please check the system path configuration.")
            return

        selected_model = self.model_combo.currentText()
        include_subdirs = "1" if self.include_subdirs_checkbox.isChecked() else "0"
        selected_format = self.format_combo.currentText()
        translate = "1" if self.translate_checkbox.isChecked() else "0"
        selected_language = self.language_combo.currentText()

        command = f"{script_path} {selected_model} {include_subdirs} {selected_format} {translate} {selected_language}"

        self.process_thread = BatchProcessThread(command)
        self.process_thread.finished.connect(self.process_finished)
        self.process_thread.start()

        self.run_button.setEnabled(False)

    def process_finished(self):
        self.run_button.setEnabled(True)
        print("Batch process completed.")


if __name__ == "__main__":
    app = QApplication([])
    main_window = MainWindow()
    main_window.show()
    sys.exit(app.exec())
