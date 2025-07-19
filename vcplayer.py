from pytgcalls import PyTgCalls
from pytgcalls.types.input_stream import InputStream, AudioPiped
from pyrogram import Client
import yt_dlp
import os

# 🚀 Load Railway env vars
API_ID = int(os.environ.get("API_ID"))
API_HASH = os.environ.get("API_HASH")
SESSION_STRING = os.environ.get("SESSION_STRING")

# 🔐 Initialize user client and PyTgCalls
vc_client = Client(
    name="vcplayer",
    api_id=API_ID,
    api_hash=API_HASH,
    session_string=SESSION_STRING
)

pytgcalls = PyTgCalls(vc_client)

# 🎶 Stream YouTube audio to group VC
async def stream_youtube(chat_id, query):
    ydl_opts = {
        'format': 'bestaudio',
        'quiet': True,
        'noplaylist': True
    }

    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        info = ydl.extract_info(query, download=False)
        url = info['url']
        title = info.get('title', 'Unknown title')

    await pytgcalls.join_group_call(
        chat_id,
        InputStream(AudioPiped(url)),
        stream_type="local_stream"
    )

    return title
