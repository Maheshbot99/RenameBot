"""lokaman"""
from pyrogram.types import (InlineKeyboardButton, InlineKeyboardMarkup,ForceReply)
from pyrogram import Client , filters

@Client.on_callback_query(filters.regex('kingmsaa'))
async def upgrade(bot,update):
	text = """**ᴩᴀyᴍᴇɴᴛ ᴅɪᴛᴇʟꜱ **

**⌾  ᴍy ɴᴀᴍᴇ ɪꜱ - ᴍᴀʜᴇꜱʜ ꜱ**

**⌾  ᴩʜᴏɴᴇ ᴩᴀy - ᴜᴩɪ :-** ```maheshs458@ybl```

**⌾  ᴩᴀyᴛᴍ - ᴜᴩɪ :-** ```mahesh.s458@paytm```

**⌾  ᴩᴀyᴛᴍ ᴅɪʀᴇᴄᴛ ʟɪɴᴋ :- [🄲🄻🄸🄲🄺 🅃🄾 🄿🄰🅈](https://p.paytm.me/xCTH/6pd91cj8)**

**🇳  🇴 🇹 🇪   :- ᴀꜰᴛᴇʀ ᴩᴀyᴍᴇɴᴛ ꜱᴇɴᴅ ꜱᴄʀᴇᴇɴ ꜱʜᴏᴛ'ꜱ ᴏꜰ ᴩᴀyᴍᴇɴᴛ ᴛᴏ ᴍᴇ - @MaHi_458**"""
	keybord = InlineKeyboardMarkup([[ 
        			InlineKeyboardButton('• ʙᴀᴄᴋ •', callback_data='start')],[InlineKeyboardButton('Cʟᴏsᴇ', callback_data='cancel')  ]])
	await update.message.edit(text = text,reply_markup = keybord)
	

@Client.on_message(filters.private & filters.command(["kingmsaa"]))
async def upgradecm(bot,message):
	text = """**ᴩᴀyᴍᴇɴᴛ ᴅɪᴛᴇʟꜱ **

**⌾  ᴍy ɴᴀᴍᴇ ɪꜱ - ᴍᴀʜᴇꜱʜ ꜱ**

**⌾  ᴩʜᴏɴᴇ ᴩᴀy - ᴜᴩɪ :-** ```maheshs458@ybl```

**⌾  ᴩᴀyᴛᴍ - ᴜᴩɪ :-** ```mahesh.s458@paytm```

**⌾  ᴩᴀyᴛᴍ ᴅɪʀᴇᴄᴛ ʟɪɴᴋ :- [🄲🄻🄸🄲🄺 🅃🄾 🄿🄰🅈](https://p.paytm.me/xCTH/6pd91cj8)**

**🇳  🇴 🇹 🇪   :- ᴀꜰᴛᴇʀ ᴩᴀyᴍᴇɴᴛ ꜱᴇɴᴅ ꜱᴄʀᴇᴇɴ ꜱʜᴏᴛ'ꜱ ᴏꜰ ᴩᴀyᴍᴇɴᴛ ᴛᴏ ᴍᴇ - @MaHi_458**"""
	keybord = InlineKeyboardMarkup([[ 
        			InlineKeyboardButton('• ʙᴀᴄᴋ •', callback_data='start')],[InlineKeyboardButton('Cʟᴏsᴇ', callback_data='cancel')  ]])
	await message.reply_text(text = text,reply_markup = keybord)
