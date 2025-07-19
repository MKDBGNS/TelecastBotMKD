from pyrogram import Client, filters
import os
import logging

logging.basicConfig(level=logging.INFO)

BOT_TOKEN = os.environ.get("BOT_TOKEN")
API_ID = int(os.environ.get("API_ID"))
API_HASH = os.environ.get("API_HASH")

bot = Client("TelecastBotMKD", api_id=API_ID, api_hash=API_HASH, bot_token=BOT_TOKEN)

@bot.on_message(filters.command("ping"))
async def ping_handler(_, message):
    print("🟡 /ping received")
    await message.reply_text("🏓 Pong!")

@bot.on_message(filters.command("start"))
async def start_handler(_, message):
    print("🟡 /start received")
    await message.reply_text("✅ Bot is alive!")

@bot.on_message()
async def catch_all(_, message):
    print(f"🔍 Received message: {message.text}")

bot.run()
