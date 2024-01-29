from gtts import gTTS

class TTS:
    def __init__(self):
        self.file_path = "./example.mp3"
        self.language = "de"

    def run(self, text):
        myobj = gTTS(text=text, lang=self.language, slow=False)
        myobj.save(self.file_path)


