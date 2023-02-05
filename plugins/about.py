import os 
from pyrogram import Client, filters
token = os.environ.get('TOKEN','')
botid = token.split(':')[0]
from helper.database import botdata, find_one, total_user

from helper.progress import humanbytes

@Client.on_message(filters.private & filters.command(["about"]))
async def start(client,message):
	botdata(int(botid))
	data = find_one(int(botid))
	total_rename = data["total_rename"]
	total_size = data["total_size"]
	await message.reply_text(f"Owner :- <a href='https://t.me/MaHi_458'>👤 MAHESH 👤</a>\nPAYTM LINK :- <a href='https://t.me/MaHi_458'>🎫 PAYTM 🎫</a>\nOwner  :- MAHESH\nUPI I'D :- maheshs458@ybl\nServer :- India\nTotal Renamed File :- {total_rename}\nTotal Size Renamed :- {humanbytes(int(total_size))} \n\n Thank You **<a href='https://t.me/MaHi_458'>👤 MAHESH 👤</a>** For Your Hard Work \n\n❤️ We Love You <a href='https://t.me/MaHi_458'>**👤 MAHESH 👤**</a> ❤️",quote=True)
