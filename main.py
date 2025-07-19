from pyrogram import Client, filters, idle
from vcplayer import stream_youtube, pytgcalls, vc_client
import os
import asyncio

BOT_TOKEN = os.environ.get("BOT_TOKEN")
API_ID = int(os.environ.get("API_ID"))
API_HASH = os.environ.get("API_HASH")

bot = Client("TelecastBotMKD", api_id=API_ID, api_hash=API_HASH, bot_token=BOT_TOKEN)

@bot.on_message(filters.command("ping"))
async def ping_handler(_, message):
    await message.reply_text("🎯 Pong!")

@bot.on_message(filters.command("start"))
async def start_handler(_, message):
    await message.reply_text("✅ Bot is alive!")

@bot.on_message(filters.command("play"))
async def play_handler(_, message):
    vc_chat = message.chat.id
    query = message.text.split(" ", 1)[1]
    title = await stream_youtube(vc_chat, query)
    await message.reply(f"🎶 Streaming: {title}")

async def main():
    await vc_client.start()
    await pytgcalls.start()
    await bot.start()
    await idle()
    await bot.stop()
    await vc_client.stop()

if __name__ == "__main__":
    asyncio.run(main())
