"""lokaman"""
from pyrogram.types import (InlineKeyboardButton, InlineKeyboardMarkup,ForceReply)
from pyrogram import Client , filters

@Client.on_callback_query(filters.regex('settings'))
async def upgrade(bot,update):
	text = """ **⚙️ ꜱᴇᴛᴛɪɴɢꜱ**

**ᴄᴏɴꜰɪɢᴜʀᴇ ꜱᴇᴛᴛɪɴɢꜱ ᴀꜱ yᴏᴜʀ ᴡɪꜱʜ**"""
	keybord = InlineKeyboardMarkup([[ 
        			InlineKeyboardButton("• ᴛʜᴜᴍʙɴᴀɪʟ ꜱᴇᴛᴛɪɴɢꜱ •",callback_data = "zdogrocky")], 
        			[InlineKeyboardButton("• ᴄᴀᴩᴛɪᴏɴ ꜱᴇᴛᴛɪɴɢꜱ •",callback_data = "21k1"),
        			InlineKeyboardButton("• ᴩʀᴇᴍɪᴜᴍ ᴩʟᴀɴꜱ •",callback_data = "king5461")],[InlineKeyboardButton("• ᴄʟᴏꜱᴇ •",callback_data = "cancel")  ]])
	await update.message.edit(text = text,reply_markup = keybord)
	

@Client.on_message(filters.private & filters.command(["settings"]))
async def upgradecm(bot,message):
	text = """ **⚙️ ꜱᴇᴛᴛɪɴɢꜱ**

**ᴄᴏɴꜰɪɢᴜʀᴇ ꜱᴇᴛᴛɪɴɢꜱ ᴀꜱ yᴏᴜʀ ᴡɪꜱʜ**"""
	keybord = InlineKeyboardMarkup([[ 
        			InlineKeyboardButton("• ᴛʜᴜᴍʙɴᴀɪʟ ꜱᴇᴛᴛɪɴɢꜱ •",callback_data = "zdogrocky")], 
        			[InlineKeyboardButton("• ᴄᴀᴩᴛɪᴏɴ ꜱᴇᴛᴛɪɴɢꜱ •",callback_data = "21k1"),
        			InlineKeyboardButton("• ᴩʀᴇᴍɪᴜᴍ ᴩʟᴀɴꜱ •",callback_data = "king5461")],[InlineKeyboardButton("• ᴄʟᴏꜱᴇ •",callback_data = "cancel")  ]])
	await message.reply_text(text = text,reply_markup = keybord)

#thumb_settings
@Client.on_callback_query(filters.regex('kingmahi'))
async def upgrade(bot,update):
	text = """ **⚙️ ꜱᴇᴛᴛɪɴɢꜱ**

**ᴄᴏɴꜰɪɢᴜʀᴇ ꜱᴇᴛᴛɪɴɢꜱ ᴀꜱ yᴏᴜʀ ᴡɪꜱʜ**"""
	keybord = InlineKeyboardMarkup([[ 
        			InlineKeyboardButton("🥈 ꜱɪʟᴠᴇʀ",callback_data = "zdogrocky")], 
        			[InlineKeyboardButton("🏆 ɢᴏʟᴅ",callback_data = "21k1"),
        			InlineKeyboardButton("💎 ᴅɪᴀᴍᴏɴᴅ",callback_data = "king5461")],[InlineKeyboardButton("• ᴄʟᴏꜱᴇ •",callback_data = "cancel")  ]])
	await update.message.edit(text = text,reply_markup = keybord)
	

@Client.on_message(filters.private & filters.command(["kingmahi"]))
async def upgradecm(bot,message):
	text = """ **⚙️ ꜱᴇᴛᴛɪɴɢꜱ**

**ᴄᴏɴꜰɪɢᴜʀᴇ ꜱᴇᴛᴛɪɴɢꜱ ᴀꜱ yᴏᴜʀ ᴡɪꜱʜ**"""
	keybord = InlineKeyboardMarkup([[ 
        			InlineKeyboardButton("🥈 ꜱɪʟᴠᴇʀ",callback_data = "zdogrocky")], 
        			[InlineKeyboardButton("🏆 ɢᴏʟᴅ",callback_data = "21k1"),
        			InlineKeyboardButton("💎 ᴅɪᴀᴍᴏɴᴅ",callback_data = "king5461")],[InlineKeyboardButton("• ᴄʟᴏꜱᴇ •",callback_data = "cancel")  ]])
	await message.reply_text(text = text,reply_markup = keybord)

#caption_setting
@Client.on_callback_query(filters.regex('qingdog'))
async def upgrade(bot,update):
	text = """ **⚙️ ꜱᴇᴛᴛɪɴɢꜱ**

**ᴄᴏɴꜰɪɢᴜʀᴇ ꜱᴇᴛᴛɪɴɢꜱ ᴀꜱ yᴏᴜʀ ᴡɪꜱʜ**"""
	keybord = InlineKeyboardMarkup([[ 
        			InlineKeyboardButton("🥈 ꜱɪʟᴠᴇʀ",callback_data = "zdogrocky")], 
        			[InlineKeyboardButton("🏆 ɢᴏʟᴅ",callback_data = "21k1"),
        			InlineKeyboardButton("💎 ᴅɪᴀᴍᴏɴᴅ",callback_data = "king5461")],[InlineKeyboardButton("• ᴄʟᴏꜱᴇ •",callback_data = "cancel")  ]])
	await update.message.edit(text = text,reply_markup = keybord)
	

@Client.on_message(filters.private & filters.command(["qingdog"]))
async def upgradecm(bot,message):
	text = """ **⚙️ ꜱᴇᴛᴛɪɴɢꜱ**

**ᴄᴏɴꜰɪɢᴜʀᴇ ꜱᴇᴛᴛɪɴɢꜱ ᴀꜱ yᴏᴜʀ ᴡɪꜱʜ**"""
	keybord = InlineKeyboardMarkup([[ 
        			InlineKeyboardButton("🥈 ꜱɪʟᴠᴇʀ",callback_data = "zdogrocky")], 
        			[InlineKeyboardButton("🏆 ɢᴏʟᴅ",callback_data = "21k1"),
        			InlineKeyboardButton("💎 ᴅɪᴀᴍᴏɴᴅ",callback_data = "king5461")],[InlineKeyboardButton("• ᴄʟᴏꜱᴇ •",callback_data = "cancel")  ]])
	await message.reply_text(text = text,reply_markup = keybord)
