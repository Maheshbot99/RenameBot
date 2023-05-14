"""lokaman"""
from pyrogram.types import (InlineKeyboardButton, InlineKeyboardMarkup,ForceReply)
from pyrogram import Client , filters

@Client.on_callback_query(filters.regex('upgrade'))
async def upgrade(bot,update):
	text = """ """
	keybord = InlineKeyboardMarkup([[ 
        			InlineKeyboardButton("👤 MAHESH 👤",url = "https://t.me/MaHi_458Bot")], 
        			[InlineKeyboardButton("Cancel",callback_data = "cancel")  ]])
	await update.message.edit(text = text,reply_markup = keybord)
	

@Client.on_message(filters.private & filters.command(["upgrade"]))
async def upgradecm(bot,message):
	text = """ """
	keybord = InlineKeyboardMarkup([[ 
        			InlineKeyboardButton("👤  MAHESH  👤",url = "https://t.me/MaHi_458Bot")], 
        			[InlineKeyboardButton("🎫  PAYTM  🎫",url = "https://p.paytm.me/xCTH/6pd91cj8"),
        			InlineKeyboardButton('🏠 Your Plan 🏠', callback_data='myplan')],[InlineKeyboardButton("Cancel",callback_data = "cancel")  ]])
	await message.reply_text(text = text,reply_markup = keybord)
