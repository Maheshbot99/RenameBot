"""lokaman"""
from pyrogram.types import (InlineKeyboardButton, InlineKeyboardMarkup,ForceReply)
from pyrogram import Client , filters

@Client.on_callback_query(filters.regex('21k1'))
async def upgrade(bot,update):
	text = """ **🏷 ᴘʟᴀɴ** :- Gold 🏆 

**⌾ ᴅᴀɪʟʏ ᴜᴘʟᴏᴀᴅ** :- 50.0 GB
**⌾ ᴛɪᴍᴇ ɢᴀᴘ** :- 0 minutes
**⌾ 4ɢʙ sᴜᴘᴘᴏʀᴛ** :- True
**⌾ ᴘᴀʀᴀʟʟᴇʟ ᴘʀᴏᴄᴇss** :- 6
**⌾ ᴠᴀʟɪᴅɪᴛʏ** :- 30 Days

**💰 ᴘʀɪᴄᴇ 100₹ ᴘᴇʀ ᴍᴏɴᴛʜ**"""
	keybord = InlineKeyboardMarkup([[ 
        			InlineKeyboardButton("💳  ᴜᴩɢʀᴀᴅᴇ",url = "https://graph.org/Subscription-05-14-3")], 
        			[InlineKeyboardButton("• ʙᴀᴄᴋ •",callback_data = "upgrade")  ]])
	await update.message.edit(text = text,reply_markup = keybord)
	

@Client.on_message(filters.private & filters.command(["21k1"]))
async def upgradecm(bot,message):
	text = """ **🏷 ᴘʟᴀɴ** :- Gold 🏆 

**⌾ ᴅᴀɪʟʏ ᴜᴘʟᴏᴀᴅ** :- 50.0 GB
**⌾ ᴛɪᴍᴇ ɢᴀᴘ** :- 0 minutes
**⌾ 4ɢʙ sᴜᴘᴘᴏʀᴛ** :- True
**⌾ ᴘᴀʀᴀʟʟᴇʟ ᴘʀᴏᴄᴇss** :- 6
**⌾ ᴠᴀʟɪᴅɪᴛʏ** :- 30 Days

**💰 ᴘʀɪᴄᴇ 100₹ ᴘᴇʀ ᴍᴏɴᴛʜ**"""
	keybord = InlineKeyboardMarkup([[ 
        			InlineKeyboardButton("💳  ᴜᴩɢʀᴀᴅᴇ",url = "https://graph.org/Subscription-05-14-3")], 
        			[InlineKeyboardButton("• ʙᴀᴄᴋ •",callback_data = "upgrade")  ]])
	await message.reply_text(text = text,reply_markup = keybord)
