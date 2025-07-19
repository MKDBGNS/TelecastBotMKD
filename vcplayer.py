from pytgcalls import PyTgCalls
from pytgcalls.types.input_stream import InputStream, AudioPiped
from pyrogram import Client
import yt_dlp

# Initialize audio client
vc_client = Client("vcbot")
pytgcalls = PyTgCalls(vc_client)

# Join VC and stream audio
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
        InputStream(
            AudioPiped(url)
        ),
        stream_type="local_stream"
    )

    return title
