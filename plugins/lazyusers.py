import os 
from pyrogram import Client, filters
from pyrogram.types import ( InlineKeyboardButton, InlineKeyboardMarkup)
token = os.environ.get('TOKEN','')
botid = token.split(':')[0]
ADMIN = int(os.environ.get("ADMIN", ""))

from helper.database import botdata, find_one, total_user,getid

from helper.progress import humanbytes

@Client.on_message(filters.private & filters.user(ADMIN)  & filters.command(["users"]))
async def start(client,message):
	botdata(int(botid))
	data = find_one(int(botid))
	total_rename = data["total_rename"]
	total_size = data["total_size"]
	id = str(getid())
	ids = id.split(',')

	await message.reply_text(f"**⚡️ ᴀʟʟ ɪᴅꜱ** : {ids}\n\n**⚡️ ᴛᴏᴛᴀʟ ᴜꜱᴇʀꜱ** :- {total_user()}\n\n**⚡️ ᴛᴏᴛᴀʟ ʀᴇɴᴀᴍᴇᴅ ꜰɪʟʀꜱ**:- {total_rename}\n**ᴛᴏᴛᴇʟ ʀᴇɴᴀᴍᴇᴅ ꜱɪᴢᴇ** :- {humanbytes(int(total_size))}",quote=True,
                             reply_markup= InlineKeyboardMarkup([[InlineKeyboardButton("• ᴄʟᴏꜱᴇ ᴍᴇɴᴜ •", callback_data="cancel")]]) 
                             )
