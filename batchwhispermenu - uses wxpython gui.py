import subprocess
import shutil
import wx


class MainWindow(wx.Frame):
    def __init__(self):
        super().__init__(None, title="Whisper GUI")

        # Initialize variables
        self.model_options = ["tiny.en", "tiny", "base.en", "base", "small.en", "small",
                              "medium.en", "medium", "large", "large-v1", "large-v2"]
        self.format_options = ["txt", "vtt", "srt", "tsv", "json", "all"]
        self.language_options = [
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
            "Turkmen", "Ukrainian", "Urdu", "Uzbek", "Valencian", "Vietnamese", "Welsh", "Yiddish", "Yoruba"
        ]

        panel = wx.Panel(self)
        vbox = wx.BoxSizer(wx.VERTICAL)

        self.model_combo = wx.ComboBox(panel, choices=self.model_options)
        self.format_combo = wx.ComboBox(panel, choices=self.format_options)
        self.include_subdirs_checkbox = wx.CheckBox(panel, label="Include subdirectories")
        self.translate_checkbox = wx.CheckBox(panel, label="Translate to English")
        self.language_combo = wx.ComboBox(panel, choices=self.language_options)
        self.run_button = wx.Button(panel, label="Run")

        self.translate_checkbox.Bind(wx.EVT_CHECKBOX, self.toggle_language_menu)
        self.run_button.Bind(wx.EVT_BUTTON, self.run_batch_script)

        vbox.Add(wx.StaticText(panel, label="Choose the Whisper model:"))
        vbox.Add(self.model_combo, flag=wx.EXPAND | wx.ALL, border=5)
        vbox.Add(wx.StaticText(panel, label="Choose the output format:"))
        vbox.Add(self.format_combo, flag=wx.EXPAND | wx.ALL, border=5)
        vbox.Add(self.include_subdirs_checkbox, flag=wx.ALL, border=5)
        vbox.Add(self.translate_checkbox, flag=wx.ALL, border=5)
        vbox.Add(wx.StaticText(panel, label="Choose the source language:"))
        vbox.Add(self.language_combo, flag=wx.EXPAND | wx.ALL, border=5)
        vbox.Add(self.run_button, flag=wx.EXPAND | wx.ALL, border=5)

        panel.SetSizer(vbox)
        self.toggle_language_menu()

        self.Show()

    def toggle_language_menu(self, event=None):
        self.language_combo.Enable(self.translate_checkbox.GetValue())

    def run_batch_script(self, event):
        script_name = "batchwhisper.bat"

        script_path = shutil.which(script_name)
        if script_path is None:
            wx.MessageBox("batchwhisper.bat not found in the system path. Please check the system path configuration.",
                          "Error", wx.OK | wx.ICON_ERROR)
            return

        selected_model = self.model_combo.GetValue()
        include_subdirs = "1" if self.include_subdirs_checkbox.GetValue() else "0"
        selected_format = self.format_combo.GetValue()
        translate = "1" if self.translate_checkbox.GetValue() else "0"
        selected_language = self.language_combo.GetValue()

        command = f"{script_path} {selected_model} {include_subdirs} {selected_format} {translate} {selected_language}"
        subprocess.run(command, shell=True)


if __name__ == '__main__':
    app = wx.App()
    main_window = MainWindow()
    app.MainLoop()
