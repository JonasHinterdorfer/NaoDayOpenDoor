import json

import requests


class STT:
    def __init__(self):
        self.APIKey = "ETQDICN7RQWZ6NRXNYA3Q3JCL9U66DKM"
        self.FileType = "wav"
        self.Language = "de"
        self.FilePath = "./rec.wav"

    def run(self):
        url = "https://transcribe.whisperapi.com"
        headers = {
            'Authorization': 'Bearer ' + self.APIKey
        }
        file = {'file': open(self.FilePath, 'rb')}
        data = {
            "fileType": self.FileType,
            "diarization": "false",
            "numSpeakers": "2",
            "language": self.Language,
            "task": "transcribe",
        }
        response = requests.post(url, headers=headers, files=file, data=data)
        return json.loads(response.content).get('text')
