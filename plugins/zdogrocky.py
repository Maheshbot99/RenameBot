"""lokaman"""
from pyrogram.types import (InlineKeyboardButton, InlineKeyboardMarkup,ForceReply)
from pyrogram import Client , filters

@Client.on_callback_query(filters.regex('zdogrocky'))
async def upgrade(bot,update):
	text = """ """
	keybord = InlineKeyboardMarkup([[ 
        			InlineKeyboardButton("👤 MAHESH 👤",url = "https://t.me/MaHi_458Bot")], 
        			[InlineKeyboardButton("• ʙᴀᴄᴋ •",callback_data = "upgrade")  ]])
	await update.message.edit(text = text,reply_markup = keybord)
	

@Client.on_message(filters.private & filters.command(["zdogrocky"]))
async def upgradecm(bot,message):
	text = """ """
	keybord = InlineKeyboardMarkup([[ 
        			InlineKeyboardButton("👤  MAHESH  👤",url = "https://t.me/MaHi_458Bot")], 
        			[InlineKeyboardButton("• ʙᴀᴄᴋ •",callback_data = "upgrade")  ]])
	await message.reply_text(text = text,reply_markup = keybord)
