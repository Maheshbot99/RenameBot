"""lokaman"""
from pyrogram.types import (InlineKeyboardButton, InlineKeyboardMarkup,ForceReply)
from pyrogram import Client , filters

@Client.on_callback_query(filters.regex('upgrade'))
async def upgrade(bot,update):
	text = """ **🏷 ᴄᴜʀʀᴇɴᴛ ᴘʟᴀɴ** :- Free

**⌾ ᴅᴀɪʟʏ ᴜᴘʟᴏᴀᴅ** :- 4.01 GB
**⌾ ᴛɪᴍᴇ ɢᴀᴘ** :- 1 min
**⌾ 4ɢʙ sᴜᴘᴘᴏʀᴛ** :- False
**⌾ ᴘᴀʀᴀʟʟᴇʟ ᴘʀᴏᴄᴇss** :- 1 
**⌾ ᴠᴀʟɪᴅɪᴛʏ** :- Life Time"""
	keybord = InlineKeyboardMarkup([[ 
        			InlineKeyboardButton("Cancel",callback_data = "cancel")], 
        			[InlineKeyboardButton("Cancel",callback_data = "cancel"),
        			InlineKeyboardButton("Cancel",callback_data = "cancel")],[InlineKeyboardButton("Cancel",callback_data = "cancel")  ]])
	await update.message.edit(text = text,reply_markup = keybord)
	

@Client.on_message(filters.private & filters.command(["upgrade"]))
async def upgradecm(bot,message):
	text = """ """
	keybord = InlineKeyboardMarkup([[ 
        			InlineKeyboardButton("Cancel",callback_data = "cancel")], 
        			[InlineKeyboardButton("Cancel",callback_data = "cancel"),
        			InlineKeyboardButton("Cancel",callback_data = "cancel")],[InlineKeyboardButton("Cancel",callback_data = "cancel")  ]])
	await message.reply_text(text = text,reply_markup = keybord)
