#(©)Codexbotz

from pyrogram import __version__
from bot import Bot
from config import OWNER_ID
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton, CallbackQuery

@Bot.on_callback_query()
async def cb_handler(client: Bot, query: CallbackQuery):
    data = query.data
    if data == "about":
        await query.message.edit_text(
            text = f"<b>○ ᴘʀᴏᴘʀɪéᴛᴀɪʀᴇ : <a href='tg://user?id={OWNER_ID}'>Mikey</a>\n○ ᴍᴇꜱ ᴍɪꜱᴇꜱ à ᴊᴏᴜʀ : <a href='https://t.me/CodeFlix_Bots'>ᴄᴏᴅᴇꜰʟɪx ʙᴏᴛꜱ</a>\n○ ᴍɪꜱᴇꜱ à ᴊᴏᴜʀ ᴅᴇꜱ ꜰɪʟᴍꜱ: <a href='https://t.me/Team_Netflix'>ᴛᴇᴀᴍ ɴᴇᴛꜰʟɪx</a>\n○ ɴᴏᴛʀᴇ ᴄᴏᴍᴍᴜɴᴀᴜᴛé : <a href='https://t.me/otakuflix_network'>ᴏᴛᴀᴋᴜꜰʟɪx ɴᴇᴛᴡᴏʀᴋ</a>\n○ ᴄʜᴀᴛ ᴀɴɪᴍᴇ : <a href='https://t.me/weebzonex'>ᴡᴇᴇʙ ᴢᴏɴᴇ</a></b>",
            disable_web_page_preview = True,
            reply_markup = InlineKeyboardMarkup(
                [
                    [
                    InlineKeyboardButton("⚡️ ꜰᴇʀᴍᴇʀ", callback_data = "close"),
                    InlineKeyboardButton('🍁 ᴘʀᴇᴍɪᴜᴍ', url='https://t.me/OtakuFlix_Network/4639')
                    ]
                ]
            )
        )
    elif data == "close":
        await query.message.delete()
        try:
            await query.message.reply_to_message.delete()
        except:
            pass
