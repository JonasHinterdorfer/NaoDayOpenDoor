import speech_recognition as sr

class STT:
    def __init__(self):
        self.recognizer = sr.Recognizer()
        self.FilePath = "./rec.wav"

    def run(self):
        return self.transcribe_audio()

    def transcribe_audio(self):
        with sr.AudioFile(self.FilePath) as source:
            audio = self.recognizer.record(source)
        try:
            text = self.recognizer.recognize_google(audio, language="de-DE")
            return text
        except sr.UnknownValueError:
            return "Google Speech Recognition could not understand audio"
        except sr.RequestError as e:
            return f"Could not request results from Google Speech Recognition service; {e}"