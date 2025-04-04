from pyrogram import __version__
from bot import Bot
from config import OWNER_ID
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton, CallbackQuery



@Bot.on_callback_query()
async def cb_handler(client: Bot, query: CallbackQuery):
    data = query.data
    if data == "about":
        await query.message.edit_text(
            text = f"<b>🤖 My Name :</b> <a href='https://t.me/NeonFilesBot'><b>NeonFilesBot</b></a> \n<b>📝 Language :</b> <a href='https://python.org'><b>Python 3</b></a> \n<b>📚 Library :</b> <a href='https://pyrogram.org'><b>Pyrogram {__version__}</b></a> \n<b>🚀 Server :</b> <a href='https://heroku.com'><b>Heroku</b></a> \n<b>📢 Channel :</b> <a href='https://t.me/NeonFiles'><b>NeonFiles</b></a> \n<b>🧑‍💻 Developer :</b> <a href='tg://user?id={OWNER_ID}'><b>NeonAnurag</b></a>",
            disable_web_page_preview = True,
            reply_markup = InlineKeyboardMarkup(
                [
                    [
                        InlineKeyboardButton("🔒 Close", callback_data = "close")
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





# MyselfNeon
# Don't Remove Credit 🥺
# Telegram Channel @NeonFiles
# Second Channel @AnimeZerox
# Developer @NeonAn23
