"""lokaman"""
from pyrogram.types import (InlineKeyboardButton, InlineKeyboardMarkup,ForceReply)
from pyrogram import Client , filters

@Client.on_callback_query(filters.regex('zdogrocky1'))
async def upgrade(bot,update):
	text = """ """
	keybord = InlineKeyboardMarkup([[ 
        			InlineKeyboardButton("💳  ᴜᴩɢʀᴀᴅᴇ",url = "https://graph.org/Buy-05-14")], 
        			[InlineKeyboardButton("• ʙᴀᴄᴋ •",callback_data = "upgrade")  ]])
	await update.message.edit(text = text,reply_markup = keybord)
	

@Client.on_message(filters.private & filters.command(["zdogrocky1"]))
async def upgradecm(bot,message):
	text = """ """
	keybord = InlineKeyboardMarkup([[ 
        			InlineKeyboardButton("💳  ᴜᴩɢʀᴀᴅᴇ",url = "https://graph.org/Buy-05-14")], 
        			[InlineKeyboardButton("• ʙᴀᴄᴋ •",callback_data = "upgrade")  ]])
	await message.reply_text(text = text,reply_markup = keybord)
