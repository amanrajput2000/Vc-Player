import os
import sys
from datetime import datetime
from time import time

from pyrogram import Client, filters
from pyrogram.types import Message

from config import HNDLR, SUDO_USERS

# System Uptime
START_TIME = datetime.utcnow()
TIME_DURATION_UNITS = (
    ('Week', 60 * 60 * 24 * 7),
    ('Day', 60 * 60 * 24),
    ('Hour', 60 * 60),
    ('Min', 60),
    ('Sec', 1)
)

async def _human_time_duration(seconds):
    if seconds == 0:
        return "inf"
    parts = []
    for unit, div in TIME_DURATION_UNITS:
        amount, seconds = divmod(int(seconds), div)
        if amount > 0:
            parts.append("{} {}{}".format(amount, unit, "" if amount == 1 else ""))
    return ", ".join(parts)


@Client.on_message(filters.command(["ping"], prefixes=f"{HNDLR}"))
async def ping(client, m: Message):
    start = time()
    current_time = datetime.utcnow()
    m_reply = await m.reply_text("⚡")
    delta_ping = time() - start
    uptime_sec = (current_time - START_TIME).total_seconds()
    uptime = await _human_time_duration(int(uptime_sec))
    await m_reply.edit(
        f"<b>Panchi muusic userbot is Online💗</b> `{delta_ping * 1000:.3f} ms` \n<b>⏳Uptime </b> - `{uptime}`"
    )


@Client.on_message(
    filters.user(SUDO_USERS) & filters.command(["restart"], prefixes=f"{HNDLR}")
)
async def restart(client, m: Message):
    await m.delete()
    loli = await m.reply("1")
    await loli.edit("2")
    await loli.edit("3")
    await loli.edit("4")
    await loli.edit("5")
    await loli.edit("6")
    await loli.edit("7")
    await loli.edit("8")
    await loli.edit("9")
    await loli.edit("**🖥️System🖱️Restarted⌨️**")
    os.execl(sys.executable, sys.executable, *sys.argv)
    quit()


@Client.on_message(filters.command(["help"], prefixes=f"{HNDLR}"))
async def help(client, m: Message):
    await m.delete()
    HELP = f"""
<i>🤓𝗛𝗲𝗹𝗹𝗼 {m.from_user.mention}!

🛠 HELP MENU
⚡ 𝗖𝗢𝗠𝗠𝗔𝗡𝗗𝗦 🇮🇳
🥀 {HNDLR}help - to see a list of commands
🥀 {HNDLR}play [song title | link youtube | reply audio file] - to play a song
🥀 {HNDLR}vplay [video title | link youtube | reply video files] - to play videos
🥀 {HNDLR}dsong [ song name |yt link ]To download any song
🥀{HNDLR}playlist to view playlist
🥀 {HNDLR}ping - to check status
🥀 {HNDLR}resume - to continue playing a song or video
🥀 {HNDLR}pause - to pause the playback a song or video 
🥀 {HNDLR}skip - to skip songs or videos
🥀 {HNDLR}end - to end playback</i>
"""
    await m.reply(HELP)

@Client.on_message(filters.command(["Good morning", "Gud morning", "gud mrng", "ഗുഡ് മോർണിംഗ്"], prefixes=f"{HNDLR}"))
async def goodmorning(client, m: Message):
    GM = f"""
<i>🍂☕️Gøød Mørning..𝐃𝐞𝐚𝐫⏱️ 𝐇𝐚𝐯𝐞 𝐚 𝐠𝐫𝐞𝐚𝐭 𝐝𝐚𝐲..❤️</i>
"""
    await m.reply(GM)


@Client.on_message(filters.command(["Good Evening", "Gud evng", "gud evening", "ഗുഡ് ഈവനിംഗ്", "ഗുഡ് ഈവെനിംഗ്"], prefixes=f"{HNDLR}"))
async def goodevening(client, m: Message):
    GE = f"""
<i> ❤️Gøød Evening ɖʀǟʀ..☕️</i>
"""
    await m.reply(GE)


@Client.on_message(filters.command(["Good Night", "Gud nt", "gud night", "ഗുഡ് നൈറ്റ്‌", "gudnyt"], prefixes=f"{HNDLR}"))
async def goodnight(client, m: Message):
    GN = f"""
<i> 😴🛌ɢօօɖ ռɨɢɦȶ ɖɛǟʀ 🌚</i>
"""
    await m.reply(GN)
