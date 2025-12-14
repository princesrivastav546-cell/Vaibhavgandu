import os
import telebot
import requests
import time
from datetime import datetime
from flask import Flask
from threading import Thread

# Flask keep-alive
app = Flask(__name__)

@app.route('/')
def home():
    return "Bot is running"

def run_flask():
    app.run(host='0.0.0.0', port=8080)

Thread(target=run_flask, daemon=True).start()

# Bot setup
API_BASE = "https://anishexploits.site/api/api.php?key=exploits&num="
BOT_TOKEN = os.getenv("BOT_TOKEN", "8372266918:AAGMkYzH0QvmxGJVrrTXvF8nzT7KXjj1O40")

bot = telebot.TeleBot(BOT_TOKEN)

@bot.message_handler(commands=['start'])
def start(message):
    markup = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True)
    markup.add(telebot.types.KeyboardButton('📞 ENTER NUMBER'))
    bot.send_message(
        message.chat.id,
        "👋 *WELCOME TO OLIVER EXPLOITS*\n\n🔍 *Advanced Number Scanner Bot*",
        reply_markup=markup,
        parse_mode='Markdown'
    )

@bot.message_handler(func=lambda message: message.text == '📞 ENTER NUMBER')
def ask_number(message):
    bot.send_message(
        message.chat.id,
        "📤 *Send Your 10-digit Number Without +91:*\nExample: `9876543210`",
        parse_mode='Markdown'
    )

@bot.message_handler(func=lambda message: message.text.isdigit() and len(message.text) == 10)
def process_number(message):
    number = message.text.strip()
    
    msg = bot.send_message(message.chat.id, "🔍 *Scanning Database...*", parse_mode='Markdown')
    time.sleep(2)
    
    try:
        response = requests.get(f"{API_BASE}{number}", timeout=30)
        if response.status_code == 200:
            data = response.json()
            # Process data here (same as before)
            result = format_report(data, number)
        else:
            result = f"❌ Error: {response.status_code}"
    except:
        result = "❌ Connection Error"
    
    bot.delete_message(message.chat.id, msg.message_id)
    bot.send_message(message.chat.id, result, parse_mode='Markdown')

def format_report(data, number):
    # Same formatting function as before
    return "🛡️ Report for " + number

print("🤖 Bot starting...")
bot.polling(non_stop=True)
