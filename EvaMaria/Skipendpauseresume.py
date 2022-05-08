from pyrogram import Client, filters
from pyrogram.types import Message

from config import HNDLR, call_py
from EvaMaria.helpers.decorators import authorized_users_only
from EvaMaria.helpers.handlers import skip_current_song, skip_item
from EvaMaria.helpers.queues import QUEUE, clear_queue


@Client.on_message(filters.command(["skip"], prefixes=f"{HNDLR}"))
async def skip(client, m: Message):
    await m.delete()
    chat_id = m.chat.id
    if len(m.command) < 2:
        op = await skip_current_song(chat_id)
        if op == 0:
            await m.reply("**𝗞𝘂𝗰𝗵 𝗰𝗵𝗮𝗹 𝗵𝗶 𝗻𝗶 𝗿𝗵𝗮 𝘁𝗼 𝗸𝘆𝗮 𝘀𝗸𝗶𝗽 𝗸𝗿𝘂 😒!**")
        elif op == 1:
            await m.reply("**😩𝗤𝘂𝗲𝘂𝗲 𝗶𝘀 𝗲𝗺𝗽𝘁𝘆, 𝗹𝗲𝗮𝘃𝗶𝗻𝗴 𝗩𝗼𝗶𝗰𝗲 𝗰𝗵𝗮𝘁**")
        else:
            await m.reply(
                f"**⏭ Skipped** \n**🎧 𝗡𝗼𝘄 𝗽𝗹𝗮𝘆𝗶𝗻𝗴** - [{op[0]}]({op[1]}) | `{op[2]}`",
                disable_web_page_preview=True,
            )
    else:
        skip = m.text.split(None, 1)[1]
        OP = "**🗑️ Removed the following songs from the Queue: -**"
        if chat_id in QUEUE:
            items = [int(x) for x in skip.split(" ") if x.isdigit()]
            items.sort(reverse=True)
            for x in items:
                if x == 0:
                    pass
                else:
                    hm = await skip_item(chat_id, x)
                    if hm == 0:
                        pass
                    else:
                        OP = OP + "\n" + f"**#⃣{x}** - {hm}"
            await m.reply(OP)


@Client.on_message(filters.command(["end", "stop"], prefixes=f"{HNDLR}"))
async def stop(client, m: Message):
    await m.delete()
    chat_id = m.chat.id
    if chat_id in QUEUE:
        try:
            await call_py.leave_group_call(chat_id)
            clear_queue(chat_id)
            await m.reply("**😐𝗘𝗻𝗱𝗶𝗻𝗴 𝗣𝗹𝗮𝘆𝗯𝗮𝗰𝗸𝘀**")
        except Exception as e:
            await m.reply(f"**𝗘𝗥𝗥𝗢𝗥** \n`{e}`")
    else:
        await m.reply("**🤨𝗞𝘂𝗰𝗵 𝗻𝗮𝗵𝗶 𝗰𝗵𝗮𝗹 𝗿𝗵𝗮!**")


@Client.on_message(filters.command(["pause"], prefixes=f"{HNDLR}"))
async def pause(client, m: Message):
    await m.delete()
    chat_id = m.chat.id
    if chat_id in QUEUE:
        try:
            await call_py.pause_stream(chat_id)
            await m.reply(
                f"**⏸ 𝘀𝗼𝗻𝗴 𝗶𝘀 𝗽𝗮𝘂𝘀𝗲𝗱 𝗺𝗶𝘁 𝗴𝘆𝗶 𝗸𝗵𝘂𝗷𝗹𝗶😆.**\n\n• 𝗿𝗲𝘀𝘂𝗺𝗲 𝗸𝗮𝗿𝗻𝗲 𝗸𝗲 𝗹𝗶𝘆𝗲 𝘆𝗲 𝗰𝗼𝗺𝗺𝗮𝗻𝗱 𝘂𝘀𝗲 𝗸𝗿𝗼😄 » {HNDLR}resume"
            )
        except Exception as e:
            await m.reply(f"**𝗘𝗥𝗥𝗢𝗥** \n`{e}`")
    else:
        await m.reply("**🤨𝗞𝘂𝗰𝗵 𝗻𝗵𝗶 𝗰𝗵𝗮𝗹 𝗿𝗵𝗮!**")


@Client.on_message(filters.command(["resume"], prefixes=f"{HNDLR}"))
async def resume(client, m: Message):
    await m.delete()
    chat_id = m.chat.id
    if chat_id in QUEUE:
        try:
            await call_py.resume_stream(chat_id)
            await m.reply(
                f"**▶ 𝘀𝗼𝗻𝗴 𝗶𝘀 𝗿𝗲𝘀𝘂𝗺𝗲𝗱 **\n\n• 𝗳𝗶𝗿𝘀𝗲 𝗸𝗵𝘂𝗷𝗹𝗶 𝗵𝗼 𝗿𝗵𝗶 𝘁𝗼 𝗽𝗮𝘂𝘀𝗲 𝗸𝗿𝗻𝗲 𝗸𝗲 𝗹𝗶𝘆𝗲 𝘆𝗲 𝗰𝗼𝗺𝗺𝗮𝗻𝗱 𝘂𝘀𝗲 𝗸𝗿😄 » {HNDLR}pause**"
            )
        except Exception as e:
            await m.reply(f"**𝗘𝗥𝗥𝗢𝗥** \n`{e}`")
    else:
        await m.reply("**🙄 𝗞𝘂𝗰𝗵 𝗻𝗵𝗶 𝗰𝗵𝗮𝗹 𝗿𝗵𝗮 𝘁𝗼 𝗸𝘆 𝗽𝗮𝘂𝘀𝗲 𝗸𝗿𝘂!**")
