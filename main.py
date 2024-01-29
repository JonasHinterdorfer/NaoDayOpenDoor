from flask import Flask, jsonify, request

from Bot import Bot
from FileTransfer import FileTransfer
from STT import STT
from TTS import TTS

app = Flask(__name__)
ft = FileTransfer()
stt = STT()
tts = TTS()
bot = Bot()

@app.route('/', methods=['GET'])
def home():

    ft.get_recording_from_nao()
    text = stt.run()
    text = bot.send(text)
    tts.run(text)
    ft.send_audio_to_nao()
    return 200



if __name__ == '__main__':
    app.run(debug=True)