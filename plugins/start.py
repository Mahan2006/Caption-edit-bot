# Infinity Bots

from pyrogram import Client, filters

@Client.on_message(filters.command("start") & filters.private)
async def start(client, message):
  await message.reply("Hi")
