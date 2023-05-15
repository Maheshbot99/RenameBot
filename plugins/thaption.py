"""lokaman"""
from pyrogram.types import (InlineKeyboardButton, InlineKeyboardMarkup,ForceReply)
from pyrogram import Client , filters

@Client.on_callback_query(filters.regex('kingppt'))
async def upgrade(bot,update):
	text = """ **⚙️ ꜱᴇᴛᴛɪɴɢꜱ**

**ꜱᴇᴛ ᴄᴀᴩᴛɪᴏɴ ꜱᴇᴛᴛɪɴɢꜱ ᴀꜱ yᴏᴜʀ ᴡɪꜱʜ**"""
	keybord = InlineKeyboardMarkup([[ 
        			InlineKeyboardButton("ꜱᴇᴛ ᴄᴀᴩᴛɪᴏɴ",callback_data = "set_caption")], 
        			[InlineKeyboardButton("ꜱʜᴏᴡ ᴄᴀᴩᴛɪᴏɴ",callback_data = "see_caption"),
        			InlineKeyboardButton("ᴅᴇʟᴇᴛᴇ ᴄᴀᴩᴛɪᴏɴ",callback_data = "del_caption")],[InlineKeyboardButton("• ʙᴀᴄᴋ •",callback_data = "settings")  ]])
	await update.message.edit(text = text,reply_markup = keybord)
	

@Client.on_message(filters.private & filters.command(["kingppt"]))
async def upgradecm(bot,message):
	text = """ **⚙️ ꜱᴇᴛᴛɪɴɢꜱ**

**ꜱᴇᴛ ᴄᴀᴩᴛɪᴏɴ ꜱᴇᴛᴛɪɴɢꜱ ᴀꜱ yᴏᴜʀ ᴡɪꜱʜ**"""
	keybord = InlineKeyboardMarkup([[ 
        			InlineKeyboardButton("ꜱᴇᴛ ᴄᴀᴩᴛɪᴏɴ",callback_data = "set_caption")], 
        			[InlineKeyboardButton("ꜱʜᴏᴡ ᴄᴀᴩᴛɪᴏɴ",callback_data = "see_caption"),
        			InlineKeyboardButton("ᴅᴇʟᴇᴛᴇ ᴄᴀᴩᴛɪᴏɴ",callback_data = "del_caption")],[InlineKeyboardButton("• ʙᴀᴄᴋ •",callback_data = "settings")  ]])
	await message.reply_text(text = text,reply_markup = keybord)
