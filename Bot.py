import json
import requests


class Bot:
    def __init__(self):
        self.application = '4892915099683534077'
        self.instance = '48333609'
        self.history = []
        self.historylength = 3
        self.historyCharLength = 100

    def bot(self):
        message_payload = {
            'application': self.application,
            'instance': self.instance,
            'message': f"{', '.join(self.history)}"
        }
        url = "https://www.botlibre.com/rest/json/chat"
        headers = {'Content-Type': 'application/json'}

        response = requests.post(url, headers=headers, data=json.dumps(message_payload))

        if response.status_code == 200:
            print("bot response: " + json.loads(response.content).get('message'))
            return json.loads(response.content).get('message')
        return

    def send(self, text):
        self.trim_history()
        print(' ,'.join(self.history))
        self.history.append("Me: " + text)
        text = self.bot()
        self.history.append("You: " + text)
        return text

    def trim_history(self):
        self.history = self.history[:self.historylength]
        self.history = [s[:self.historyCharLength] for s in self.history]


def main():
    bot = Bot()
    while (1 == 1):
        text = input("enter text = ")
        print(bot.send(text))


if __name__ == "__main__":
    main()
