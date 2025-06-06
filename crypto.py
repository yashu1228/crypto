from flask import Flask, request
import requests

app = Flask(__name__)

BOT_TOKEN = '7562935932:AAEykieAmz4S5NypmIJN2YMjct8lM3l_YEw'
CHAT_ID = '5833845852'

def send_telegram(message):
    url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"
    payload = {
        "chat_id": CHAT_ID,
        "text": message,
        "parse_mode": "HTML"
    }
    requests.post(url, json=payload)

@app.route('/', methods=['POST'])
def webhook():
    data = request.json
    signal = data.get("signal", "UNKNOWN")
    price = data.get("price", "N/A")
    symbol = data.get("symbol", "N/A")
    time = data.get("time", "N/A")
    msg = f"<b>{signal} Signal</b>\nSymbol: {symbol}\nPrice: {price}\nTime: {time}"
    send_telegram(msg)
    return 'ok', 200
