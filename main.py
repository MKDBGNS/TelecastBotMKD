from pyrogram import Client, filters, idle
from vcplayer import stream_youtube, pytgcalls, vc_client
import os
import logging
import asyncio

logging.basicConfig(level=logging.INFO)

# 🌐 Load credentials
BOT_TOKEN = os.environ.get("BOT_TOKEN")
API_ID = int(os.environ.get("API_ID"))
API_HASH = os.environ.get("API_HASH")
SESSION_STRING = os.environ.get("SESSION_STRING")

# 🤖 Define bot client
bot = Client("TelecastBotMKD", api_id=API_ID, api_hash=API_HASH, bot_token=BOT_TOKEN)


# 🎯 Command: /ping
@bot.on_message(filters.command("ping"))
async def ping_handler(_, message):
    print("🟢 /ping received")
    await message.reply_text("🎯 Pong!")


# 📣 Command: /start
@bot.on_message(filters.command("start"))
async def start_handler(_, message):
    print("🟢 /start received")
    await message.reply_text("✅ Bot is alive!")


# 🎵 Command: /play
@bot.on_message(filters.command("play"))
async def play_command(_, message):
    print("🎧 /play triggered")
    if message.chat.type not in ["supergroup", "group"]:
        return await message.reply("❗ Use this in a group with VC.")

    query = message.text.split(" ", 1)
    if len(query) < 2:
        return await message.reply("🎵 Provide a song name or YouTube link.")

    title = await stream_youtube(message.chat.id, query[1])
    await message.reply(f"🎶 Streaming: {title}")


# 🚀 Async startup sequence
async def main():
    print("🔐 Starting VC client...")
    await vc_client.start()

    print("📞 Starting PyTgCalls...")
    await pytgcalls.start()

    print("🤖 Starting bot...")
    await bot.start()

    print("✅ All systems running! Use /start or /play to begin.")
    await idle()

    print("🛑 Shutdown initiated...")
    await bot.stop()
    await vc_client.stop()


# 🧬 Run it all
if __name__ == "__main__":
    asyncio.run(main())
