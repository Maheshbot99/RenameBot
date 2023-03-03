"""lokaman"""
from pyrogram.types import (InlineKeyboardButton, InlineKeyboardMarkup,ForceReply)
from pyrogram import Client , filters

@Client.on_callback_query(filters.regex('upgrade'))
async def upgrade(bot,update):
	text = """ **Free Plan User**
	**Daily Upload Limit 4GB**
	**4GB File Support :- No**
        **Multi File Rename :- No**
        **Price :- 0**
	
	**🥈 Silver Plan User 🥈** 
	**Daily Upload Limit 10GB**
	**4GB File Support :- Yes**
        **Multi File Rename :- Yes**
	**Price :- Rs 100 ind / 1.22$ Per Month**
	
	**🏅 Gold Plan User 🏅**
	**Daily Upload Limit 50GB**
	**4GB File Support :- Yes**
        **Multi File Rename :- Yes**
	**Price :- Rs 150 ind / 1.2$ Per Month**
	
	**💎 Diamond Plan User 💎**
	**Daily Upload Limit 100GB**
	**4GB File Support :- Yes**
        **Multi File Rename :- Yes**
	**Price :- Rs 150 ind / 1.83$ Per Month**
	
	
	**Payment :-** `maheshs458@ybl`
	
	**After Payment Send Screenshots Of  
        Payment To Admin @MaHi_458Bot**"""
	keybord = InlineKeyboardMarkup([[ 
        			InlineKeyboardButton("👤 MAHESH 👤",url = "https://t.me/MaHi_458Bot")], 
        			[InlineKeyboardButton("🎫  PAYTM  🎫",url = "https://p.paytm.me/xCTH/6pd91cj8"),
        			InlineKeyboardButton("🎫  PAYTM  🎫",url = "https://p.paytm.me/xCTH/6pd91cj8")],[InlineKeyboardButton("Cancel",callback_data = "cancel")  ]])
	await update.message.edit(text = text,reply_markup = keybord)
	

@Client.on_message(filters.private & filters.command(["upgrade"]))
async def upgradecm(bot,message):
	text = """ **Free Plan User**
	**Daily Upload Limit 4GB**
	**Daily Upload Limit 4GB**
	**4GB File Support :- No**
	**🤑Price :- 0**
	
	**🥈 Silver Plan User 🥈** 
	**Daily Upload Limit 10GB**
	**4GB File Support :- Yes**
        **Multi File Rename :- Yes**
	**🤑Price :- Rs 50 ind / 0.6$ Per Month**
	
	**🏅 Gold Plan User 🏅**
	**Daily Upload Limit 50GB**
	**4GB File Support :- Yes**
        **Multi File Rename :- Yes**
	**🤑Price :- Rs 100 ind / 1.2$ Per Month**
	
	**💎 Diamond Plan User 💎**
	**Daily Upload Limit 100GB**
	**4GB File Support :- Yes**
        **Multi File Rename :- Yes**
	**🤑Price :- Rs 150 ind / 1.8$ Per Month**
	
	
	**Payment :-** `maheshs458@ybl`
	
	**After Payment Send Screenshots Of  
        Payment To Admin @MaHi_458Bot**"""
	keybord = InlineKeyboardMarkup([[ 
        			InlineKeyboardButton("👤  MAHESH  👤",url = "https://t.me/MaHi_458Bot)], 
        			[InlineKeyboardButton("🎫  PAYTM  🎫",url = "https://p.paytm.me/xCTH/6pd91cj8"),
        			InlineKeyboardButton("🎫  PAYTM  🎫",url = "https://p.paytm.me/xCTH/6pd91cj8")],[InlineKeyboardButton("Cancel",callback_data = "cancel")  ]])
	await message.reply_text(text = text,reply_markup = keybord)
