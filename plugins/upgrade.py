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
	
	
	Payment :- *maheshs458@ybl**
	
	**𝖠𝖿𝗍𝖾𝗋 𝖯𝖺𝗒𝗆𝖾𝗇𝗍 𝖲𝖾𝗇𝖽 𝖲𝖼𝗋𝖾𝖾𝗇𝗌𝗁𝗈𝗍𝗌 𝖮𝖿  
        𝖯𝖺𝗒𝗆𝖾𝗇𝗍 𝖳𝗈 𝖠𝖽𝗆𝗂𝗇 @MaHi_458**"""
	keybord = InlineKeyboardMarkup([[ 
        			InlineKeyboardButton("👤  𝙼𝚊𝚑𝚎𝚜𝚑.𝚂  👤",url = "https://t.me/MaHi_458")], 
        			[InlineKeyboardButton("🎫   𝙿𝚊𝚢𝚃𝚖   🎫",url = "https://p.paytm.me/xCTH/6pd91cj8"),
        			InlineKeyboardButton("🎫   𝙿𝚊𝚢𝚃𝚖   🎫",url = "https://p.paytm.me/xCTH/6pd91cj8")],[InlineKeyboardButton("Cancel",callback_data = "cancel")  ]])
	await update.message.edit(text = text,reply_markup = keybord)
	

@Client.on_message(filters.private & filters.command(["upgrade"]))
async def upgradecm(bot,message):
	text = """**𝐅𝐫𝐞𝐞 𝐏𝐥𝐚𝐧 𝐔𝐬𝐞𝐫**
	**𝙳𝚊𝚒𝚕𝚢  𝚄𝚙𝚕𝚘𝚊𝚍 𝚕𝚒𝚖𝚒𝚝 4𝙶𝙱**
	**𝙿𝚛𝚒𝚌𝚎 0**
	
	**🪙 𝐒𝐢𝐥𝐯𝐞𝐫 𝐓𝐢𝐞𝐫 🪙** 
	**𝙳𝚊𝚒𝚕𝚢  𝚄𝚙𝚕𝚘𝚊𝚍  𝚕𝚒𝚖𝚒𝚝 10𝙶𝙱**
	**𝙿𝚛𝚒𝚌𝚎 𝚁𝚜 60  𝚒𝚗𝚍 / 0.7$  𝙿𝚎𝚛 𝙼𝚘𝚗𝚝𝚑**
	
	**💫 𝐆𝐨𝐥𝐝 𝐓𝐢𝐞𝐫 💫**
	**𝙳𝚊𝚒𝚕𝚢 𝚄𝚙𝚕𝚘𝚊𝚍 𝚕𝚒𝚖𝚒𝚝 50𝙶𝙱**
	**𝙿𝚛𝚒𝚌𝚎 𝚁𝚜 100  𝚒𝚗𝚍 / 1.2$  𝚙𝚎𝚛 𝙼𝚘𝚗𝚝𝚑**
	
	**💎 𝐃𝐢𝐚𝐦𝐨𝐧𝐝 💎**
	**𝙳𝚊𝚒𝚕𝚢 𝚄𝚙𝚕𝚘𝚊𝚍 𝚕𝚒𝚖𝚒𝚝 100𝙶𝙱**
	**𝙿𝚛𝚒𝚌𝚎 𝚁𝚜 199  𝚒𝚗𝚍 / 2.4$  𝚙𝚎𝚛 𝙼𝚘𝚗𝚝𝚑**
	
	
	𝐂𝐨𝐧𝐭𝐚𝐜𝐭 𝐌𝐞 :- **@MaHi_458**
	
	**𝖠𝖿𝗍𝖾𝗋 𝖯𝖺𝗒𝗆𝖾𝗇𝗍 𝖲𝖾𝗇𝖽 𝖲𝖼𝗋𝖾𝖾𝗇𝗌𝗁𝗈𝗍𝗌 𝖮𝖿  
        𝖯𝖺𝗒𝗆𝖾𝗇𝗍 𝖳𝗈 𝖠𝖽𝗆𝗂𝗇 @MaHi_458**"""
	keybord = InlineKeyboardMarkup([[ 
        			InlineKeyboardButton("👤  𝙼𝚊𝚑𝚎𝚜𝚑.𝚂  👤",url = "https://t.me/MaHi_458")], 
        			[InlineKeyboardButton("🎫   𝙿𝚊𝚢𝚃𝚖   🎫",url = "https://p.paytm.me/xCTH/6pd91cj8"),
        			InlineKeyboardButton("🎫   𝙿𝚊𝚢𝚃𝚖   🎫",url = "https://p.paytm.me/xCTH/6pd91cj8")],[InlineKeyboardButton("Cancel",callback_data = "cancel")  ]])
	await message.reply_text(text = text,reply_markup = keybord)
