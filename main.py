from pyrogram import Client, filters, idle
from vcplayer import vc_client, pytgcalls, stream_youtube
import os
import asyncio
import logging

# 🧾 Logging setup
logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")

# 🚀 Load bot credentials
BOT_TOKEN = os.environ.get("BOT_TOKEN")
API_ID = int(os.environ.get("API_ID"))
API_HASH = os.environ.get("API_HASH")

# 🤖 Initialize bot client
bot = Client("TelecastBotMKD", api_id=API_ID, api_hash=API_HASH, bot_token=BOT_TOKEN)

# 🩺 Command: /ping
@bot.on_message(filters.command("ping"))
async def ping_handler(_, message):
    logging.info("🟢 /ping received from %s", message.chat.id)
    await message.reply("🎯 Pong!")

# ✅ Command: /start
@bot.on_message(filters.command("start"))
async def start_handler(_, message):
    logging.info("🟢 /start received from %s", message.chat.id)
    await message.reply("✅ Bot is up and running!")

# 🎧 Command: /play <query>
@bot.on_message(filters.command("play"))
async def play_handler(_, message):
    if message.chat.type not in ["supergroup", "group"]:
        return await message.reply("❗ This command requires a group with an active voice chat.")

    query = message.text.split(" ", 1)
    if len(query) < 2:
        return await message.reply("🎶 Please provide a song name or YouTube link.")

    logging.info("🎧 /play triggered with query: %s", query[1])
    title = await stream_youtube(message.chat.id, query[1])
    await message.reply(f"🎵 Now playing: {title}")

# 🧬 Run everything inside a safe async loop
async def main():
    try:
        logging.info("🔐 Starting VC client...")
        vc_task = asyncio.create_task(vc_client.start())

        logging.info("📞 Starting PyTgCalls...")
        call_task = asyncio.create_task(pytgcalls.start())

        logging.info("🤖 Starting bot client...")
        await bot.start()

        # Wait for background clients to fully start
        await vc_task
        await call_task

        logging.info("✅ All services started! Listening for commands...")
        await idle()

    except Exception as e:
        logging.error(f"🚨 Startup error: {type(e).__name__} — {e}")

    finally:
        logging.info("🛑 Gracefully stopping...")
        await bot.stop()
        await vc_client.stop()

if __name__ == "__main__":
    asyncio.run(main())
