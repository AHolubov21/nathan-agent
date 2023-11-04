import requests
import websocket
import json

class SlackModule:

    def __init__(self, token):
        self.token = token
        self.headers = {
            "Content-Type": "application/json; charset=utf-8",
            "Authorization": f"Bearer {self.token}"
        }

    def get_rtm_url(self):
        response = requests.get(
            "https://slack.com/api/rtm.connect",
            headers={"Authorization": f"Bearer {self.token}"}
        )
        data = response.json()
        return data.get("url", None)

    def send_message(self, channel, text):
        data = {
            "channel": channel,
            "text": text
        }
        response = requests.post(
            "https://slack.com/api/chat.postMessage",
            headers=self.headers,
            json=data
        )
        return response.json()

    def listen(self, callback):
        def on_message(ws, message):
            callback(message)

        # Получение URL для WebSocket прямо перед его использованием
        websocket_url = self.get_rtm_url()

        ws = websocket.WebSocketApp(
            websocket_url,
            on_message=on_message
        )
        ws.run_forever()
