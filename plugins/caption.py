# Infinity Bots

from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton, Message
from pyrogram.errors import FloodWait

mv_buttons = [[
        InlineKeyboardButton('💢 Share Our Group 💢', url='http://t.me/share/url?url=Join%20@KannadaFilmsRequests%20To%20Request%20Kannada%20Movies')
    ],[
        InlineKeyboardButton('💢 Other Language 💢', url="t.me/MahanMVGroup")
    ]]
@Client.on_message(filters.document & filters.channel)
async def caption(client, message: Message):
    await message.edit("@KannadaFilmRequests\n https://t.me/MahanCreations",
          reply_markup=InlineKeyboardMarkup(mv_buttons)
