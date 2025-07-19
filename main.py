from vcplayer import stream_youtube, pytgcalls, vc_client
from pyrogram import Client, filters
import os
import logging

logging.basicConfig(level=logging.INFO)

BOT_TOKEN = os.environ.get("BOT_TOKEN")
API_ID = int(os.environ.get("API_ID"))
API_HASH = os.environ.get("API_HASH")
SESSION_STRING = os.environ.get("SESSION_STRING")
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

@bot.on_message(filters.command("play"))
async def play_command(_, message):
    if message.chat.type not in ["supergroup", "group"]:
        return await message.reply("❗ Use this in a group with VC.")

    query = message.text.split(" ", 1)
    if len(query) < 2:
        return await message.reply("🎵 Provide a song name or YouTube link.")

    # ✅ Start client before streaming
    vc_client.start()
    pytgcalls.start()

    title = await stream_youtube(message.chat.id, query[1])
    await message.reply(f"🎶 Streaming: {title}")



bot.run()
