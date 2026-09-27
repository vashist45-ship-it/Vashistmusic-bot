import os

from pyrogram import Client, filters
from pytgcalls import PyTgCalls

API_ID = int(os.environ["API_ID"])
API_HASH = os.environ["API_HASH"]
BOT_TOKEN = os.environ["BOT_TOKEN"]

app = Client(
    "vashist_music",
    api_id=API_ID,
    api_hash=API_HASH,
    bot_token=BOT_TOKEN,
)

calls = PyTgCalls(app)


@app.on_message(filters.command("start"))
async def start(_, message):
    await message.reply_text(
        "🎵 Welcome to Vashist × Music!\n\n"
        "Use /play to play music.\n"
        "/help - Commands"
    )


@app.on_message(filters.command("help"))
async def help_cmd(_, message):
    await message.reply_text(
        "🎶 Music Commands\n\n"
        "/play - Play music\n"
        "/pause - Pause\n"
        "/resume - Resume\n"
        "/stop - Stop"
    )


app.start()
calls.start()
print("🎵 Vashist Music Bot is running!")

import asyncio
asyncio.get_event_loop().run_forever()
