from pyrogram import Client, filters, idle
from vcplayer import vc_client, pytgcalls, stream_youtube
import os
import asyncio
import logging

logging.basicConfig(level=logging.INFO)

# 🌐 Load bot credentials
BOT_TOKEN = os.environ.get("BOT_TOKEN")
API_ID = int(os.environ.get("API_ID"))
API_HASH = os.environ.get("API_HASH")

# 🧠 Create bot client
bot = Client(
    name="TelecastBotMKD",
    api_id=API_ID,
    api_hash=API_HASH,
    bot_token=BOT_TOKEN
)

# 🩺 Command: /ping
@bot.on_message(filters.command("ping"))
async def ping_handler(_, message):
    logging.info("/ping command received")
    await message.reply("🎯 Pong!")

# ✅ Command: /start
@bot.on_message(filters.command("start"))
async def start_handler(_, message):
    logging.info("/start command received")
    await message.reply("✅ Bot is up and running!")

# 🎧 Command: /play [query]
@bot.on_message(filters.command("play"))
async def play_handler(_, message):
    if message.chat.type not in ["supergroup", "group"]:
        return await message.reply("❗ Use this in a group with an active voice chat.")
    
    query = message.text.split(" ", 1)
    if len(query) < 2:
        return await message.reply("🎶 Please provide a song name or YouTube link.")

    title = await stream_youtube(message.chat.id, query[1])
    await message.reply(f"🎵 Now playing: {title}")

# ⚙️ Startup & Event Loop
async def main():
    try:
        logging.info("🔐 Starting VC client...")
        await vc_client.start()

        logging.info("📞 Starting PyTgCalls...")
        await pytgcalls.start()

        logging.info("🤖 Starting bot client...")
        await bot.start()

        logging.info("✅ Bot is live! Awaiting commands...")
        await idle()

    except Exception as e:
        logging.error(f"🚨 Startup failure: {type(e).__name__} — {e}")

    finally:
        logging.info("🛑 Stopping bot and VC client...")
        await bot.stop()
        await vc_client.stop()

if __name__ == "__main__":
    asyncio.run(main())
