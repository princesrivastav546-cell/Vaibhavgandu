from flask import Flask
from threading import Thread
import time

app = Flask('')

@app.route('/')
def home():
    return "🤖 Bot is alive! | Status: ONLINE | Made with ❤️ by @platoonleaderr"

@app.route('/ping')
def ping():
    return "PONG", 200

def run():
    app.run(host='0.0.0.0', port=8080)

def keep_alive():
    t = Thread(target=run, daemon=True)
    t.start()
    print("✅ Keep-alive server started on port 8080")
