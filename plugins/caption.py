# @TheStyleKing

from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton, Message
from pyrogram.errors import FloodWait

mv_buttons = [[
        InlineKeyboardButton('š¢ Share Our Group š¢', url='http://t.me/share/url?url=Join%20@KannadaMVRequest%20To%20Request%20Kannada%20Movies')
    ],[
        InlineKeyboardButton('š¢ Join Our Official Channel š¢', url="t.me/MahanCreations")
    ]] 
@Client.on_message(filters.document & filters.channel)
async def caption(client, message: Message):
    await message.edit("Nice to meet you Here š\nāÆ āāāāāā ā§ āāāāāāā āÆ\nShare Our Group to friend's.\nāÆ āāāāāā ā§ āāāāāāā āÆ\n@KannadaMVRequest",
          reply_markup=InlineKeyboardMarkup(mv_buttons))
