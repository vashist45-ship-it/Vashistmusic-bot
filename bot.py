import os
import threading
from http.server import BaseHTTPRequestHandler, HTTPServer

from pyrogram import Client, filters
from pytgcalls import PyTgCalls


API_ID = int(os.environ["API_ID"])
API_HASH = os.environ["API_HASH"]
BOT_TOKEN = os.environ["BOT_TOKEN"]


app = Client(
    "vashist_music",
    api_id=API_ID,
    api_hash=API_HASH,
    bot_token=BOT_TOKEN
)

calls = PyTgCalls(app)


class HealthHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.end_headers()
        self.wfile.write(b"Vashist Music Bot is running!")

    def log_message(self, format, *args):
        pass


def run_web_server():
    port = int(os.environ.get("PORT", 10000))
    server = HTTPServer(("0.0.0.0", port), HealthHandler)
    server.serve_forever()


threading.Thread(target=run_web_server, daemon=True).start()


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
        "🎵 Music Commands\n\n"
        "/play - Play Music\n"
        "/pause - Pause\n"
        "/resume - Resume\n"
        "/stop - Stop"
    )


app.start()
calls.start()

print("🎵 Vashist Music Bot is running!")

import asyncio
asyncio.get_event_loop().run_forever()
