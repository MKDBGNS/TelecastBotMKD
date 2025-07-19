from pyrogram import Client, filters, idle
import logging
import os

# Load env variables
BOT_TOKEN = os.environ.get("BOT_TOKEN")
API_ID = int(os.environ.get("API_ID"))
API_HASH = os.environ.get("API_HASH")

# Optional: Show debug logs
logging.basicConfig(level=logging.INFO)

# Create the bot client
bot = Client("TelecastBotMKD", bot_token=BOT_TOKEN, api_id=API_ID, api_hash=API_HASH)

# Command: /start
@bot.on_message(filters.command("start"))
async def start_command(_, message):
    await message.reply_text("✅ Bot is active and ready!")

# Command: /ping
@bot.on_message(filters.command("ping"))
async def ping_command(_, message):
    await message.reply_text("🏓 Pong!")

# Run the bot
async def main():
    print("🟢 Bot starting...")
    await bot.start()
    me = await bot.get_me()
    print(f"🤖 Logged in as {me.username}")
    await idle()
    await bot.stop()
    print("🛑 Bot stopped.")

# For Railway’s startup
import asyncio
asyncio.run(main())
