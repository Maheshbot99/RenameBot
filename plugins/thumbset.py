"""lokaman"""
from pyrogram.types import (InlineKeyboardButton, InlineKeyboardMarkup,ForceReply)
from pyrogram import Client , filters

@Client.on_callback_query(filters.regex('kingmahip'))
async def upgrade(bot,update):
	text = """ **⚙️ ꜱᴇᴛᴛɪɴɢꜱ**

**ꜱᴇᴛ ᴛʜᴜᴍʙɴᴀɪʟ ꜱᴇᴛᴛɪɴɢꜱ ᴀꜱ yᴏᴜʀ ᴡɪꜱʜ**"""
	keybord = InlineKeyboardMarkup([[ 
        			InlineKeyboardButton("ꜱᴇᴛ ᴛʜᴜᴍʙɴᴀɪʟ",callback_data = "setthumb")], 
        			[InlineKeyboardButton("ꜱʜᴏᴡ ᴛʜᴜᴍʙɴᴀɪʟ",callback_data = "viewthumb"),
        			InlineKeyboardButton("ᴅᴇʟᴇᴛᴇ ᴛʜᴜᴍʙɴᴀɪʟ",callback_data = "delthumb")],[InlineKeyboardButton("• ᴄʟᴏꜱᴇ •",callback_data = "settings")  ]])
	await update.message.edit(text = text,reply_markup = keybord)
	

@Client.on_message(filters.private & filters.command(["kingmahip"]))
async def upgradecm(bot,message):
	text = """ **⚙️ ꜱᴇᴛᴛɪɴɢꜱ**

**ꜱᴇᴛ ᴛʜᴜᴍʙɴᴀɪʟ ꜱᴇᴛᴛɪɴɢꜱ ᴀꜱ yᴏᴜʀ ᴡɪꜱʜ**"""
	keybord = InlineKeyboardMarkup([[ 
        			InlineKeyboardButton("ꜱᴇᴛ ᴛʜᴜᴍʙɴᴀɪʟ",callback_data = "setthumb")], 
        			[InlineKeyboardButton("ꜱʜᴏᴡ ᴛʜᴜᴍʙɴᴀɪʟ",callback_data = "viewthumb"),
        			InlineKeyboardButton("ᴅᴇʟᴇᴛᴇ ᴛʜᴜᴍʙɴᴀɪʟ",callback_data = "delthumb")],[InlineKeyboardButton("• ᴄʟᴏꜱᴇ •",callback_data = "settings")  ]])
	await message.reply_text(text = text,reply_markup = keybord)
