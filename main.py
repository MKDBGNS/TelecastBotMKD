from pyrogram import Client, filters, idle
from vcplayer import vc_client, pytgcalls, stream_youtube
import os
import asyncio
import logging

# 🧾 Setup logging
logging.basicConfig(level=logging.INFO, format="%(asctime)s — %(levelname)s — %(message)s")

# 🌐 Load bot credentials from env
BOT_TOKEN = os.environ.get("BOT_TOKEN")
API_ID = int(os.environ.get("API_ID"))
API_HASH = os.environ.get("API_HASH")

# 🤖 Initialize bot client
bot = Client("TelecastBotMKD", api_id=API_ID, api_hash=API_HASH, bot_token=BOT_TOKEN)


# 🩺 Command: /ping
@bot.on_message(filters.command("ping"))
async def ping_handler(_, message):
    logging.info("🟢 /ping received from chat: %s", message.chat.id)
    await message.reply("🎯 Pong!")


# ✅ Command: /start
@bot.on_message(filters.command("start"))
async def start_handler(_, message):
    logging.info("🟢 /start received from chat: %s", message.chat.id)
    await message.reply("✅ Bot is online and ready!")


# 🎧 Command: /play [query]
@bot.on_message(filters.command("play"))
async def play_handler(_, message):
    if message.chat.type not in ["supergroup", "group"]:
        return await message.reply("❗ Use this command inside a group with an active VC.")

    query = message.text.split(" ", 1)
    if len(query) < 2:
        return await message.reply("🎵 Please provide a song name or YouTube link.")

    logging.info("🎧 /play triggered with query: %s", query[1])
    title = await stream_youtube(message.chat.id, query[1])
    await message.reply(f"🎶 Now playing: {title}")


# 🧬 Full startup sequence
async def main():
    try:
        logging.info("🔐 Starting VC client...")
        await vc_client.start()

        logging.info("📞 Starting PyTgCalls...")
        await pytgcalls.start()

        logging.info("🤖 Starting bot client...")
        await bot.start()

        logging.info("✅ All services started. Bot is ready to receive commands.")
        await idle()

    except Exception as e:
        logging.error("🚨 Startup error: %s — %s", type(e).__name__, e)

    finally:
        logging.info("🛑 Graceful shutdown initiated...")
        await bot.stop()
        await vc_client.stop()


# 🚦 Run
if __name__ == "__main__":
    asyncio.run(main())

