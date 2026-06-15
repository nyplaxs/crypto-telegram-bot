import requests

TOKEN = "8847238536:AAHAlIc7kZzx3SHSjEshzh90NK6QpZAvh70"
CHAT_ID = "@CryptoDailyFR"

def get_prices():
    url = "https://api.coingecko.com/api/v3/simple/price?ids=bitcoin,ethereum&vs_currencies=usd"
    return requests.get(url).json()

def send_message(text):
    url = f"https://api.telegram.org/bot{TOKEN}/sendMessage"
    requests.post(url, data={
        "chat_id": CHAT_ID,
        "text": text
    })

data = get_prices()

btc = data["bitcoin"]["usd"]
eth = data["ethereum"]["usd"]

message = f"""
🚀 Crypto Daily

💰 BTC: ${btc}
💰 ETH: ${eth}

⚠️ Pas un conseil financier
"""

send_message(message)
