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

@app.route('/', methods=['POST'])
def home():
    param = request.json.get('path', None)  # Replace 'param' with your actual parameter name
    if param is None:
        return jsonify({'error': 'Missing parameter: param'}), 400
    ft.file_from_rec_nao = str(param)
    ft.nao_ip = "10.0.0.24"
    ft.get_recording_from_nao()
    text = stt.run()
    text = bot.send(text)
    tts.run(text)
    text = ft.send_audio_to_nao()
    return jsonify({'path': text}), 200
    return 200


if __name__ == '__main__':
    app.run(host=ft.get_own_ip(),debug=True)