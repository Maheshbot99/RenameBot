"""lokaman"""
from pyrogram.types import (InlineKeyboardButton, InlineKeyboardMarkup,ForceReply)
from pyrogram import Client , filters

@Client.on_callback_query(filters.regex('upgrade'))
async def upgrade(bot,update):
	text = """**Free Plan User**
	**Daily Upload Limit 4GB**
	**Price :- 0**
	
	**🥈 Silver Plan User 🥈** 
	**Daily Upload Limit 10GB**
	**Price :- Rs 50 ind / 0.6$ Per Month**
	
	**🏅 Gold Plan User 🏅**
	**Daily Upload Limit 50GB**
	**Price :- Rs 100 ind / 1.2$ Per Month**
	
	**💎 Diamond Plan User 💎**
	**Daily Upload Limit 100GB **
	**Price :- Rs 150 ind / 1.8$ Per Month**
	
	
	**Payment :-** `maheshs458@ybl`
	
	**𝖠𝖿𝗍𝖾𝗋 𝖯𝖺𝗒𝗆𝖾𝗇𝗍 𝖲𝖾𝗇𝖽 𝖲𝖼𝗋𝖾𝖾𝗇𝗌𝗁𝗈𝗍𝗌 𝖮𝖿  
        𝖯𝖺𝗒𝗆𝖾𝗇𝗍 𝖳𝗈 𝖠𝖽𝗆𝗂𝗇 @MaHi_458**"""
	keybord = InlineKeyboardMarkup([[ 
        			InlineKeyboardButton("👤 MAHESH 👤",url = "https://t.me/MaHi_458")], 
        			[InlineKeyboardButton("🎫  PAYTM  🎫",url = "https://p.paytm.me/xCTH/6pd91cj8"),
        			InlineKeyboardButton("🎫  PAYTM  🎫",url = "https://p.paytm.me/xCTH/6pd91cj8")],[InlineKeyboardButton("Cancel",callback_data = "cancel")  ]])
	await update.message.edit(text = text,reply_markup = keybord)
	

@Client.on_message(filters.private & filters.command(["upgrade"]))
async def upgradecm(bot,message):
	text = """**Free Plan User**
	**Daily Upload Limit 4GB**
	**Price :- 0**
	
	**🥈 Silver Plan User 🥈** 
	**Daily Upload Limit 10GB**
	**Price :- Rs 50 ind / 0.6$ Per Month**
	
	**🏅 Gold Plan User 🏅**
	**Daily Upload Limit 50GB**
	**Price :- Rs 100 ind / 1.2$ Per Month**
	
	**💎 Diamond Plan User 💎**
	**Daily Upload Limit 100GB **
	**Price :- Rs 150 ind / 1.8$ Per Month**
	
	
	**Payment :-** `maheshs458@ybl`
	
	**𝖠𝖿𝗍𝖾𝗋 𝖯𝖺𝗒𝗆𝖾𝗇𝗍 𝖲𝖾𝗇𝖽 𝖲𝖼𝗋𝖾𝖾𝗇𝗌𝗁𝗈𝗍𝗌 𝖮𝖿  
        𝖯𝖺𝗒𝗆𝖾𝗇𝗍 𝖳𝗈 𝖠𝖽𝗆𝗂𝗇 @MaHi_458**"""
	keybord = InlineKeyboardMarkup([[ 
        			InlineKeyboardButton("👤  MAHESH  👤",url = "https://t.me/MaHi_458")], 
        			[InlineKeyboardButton("🎫  PAYTM  🎫",url = "https://p.paytm.me/xCTH/6pd91cj8"),
        			InlineKeyboardButton("🎫  PAYTM  🎫",url = "https://p.paytm.me/xCTH/6pd91cj8")],[InlineKeyboardButton("Cancel",callback_data = "cancel")  ]])
	await message.reply_text(text = text,reply_markup = keybord)
