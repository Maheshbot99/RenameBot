"""lokaman"""
from pyrogram.types import (InlineKeyboardButton, InlineKeyboardMarkup,ForceReply)
from pyrogram import Client , filters

@Client.on_callback_query(filters.regex('help'))
async def upgrade(bot,update):
	text = """ 📚 Available Commands:

➢ /start - check i'm alive 

➢ /plans - check available plan info

➢ /set_caption - To add your custom caption 

➢ /see_caption - To see your custom caption

➢ /del_caption - To delete your custom caption

➢ /viewthumb - To see your custom thumbnail

➢ /delthumb - To delete your custom thumbnail

• upgrade your premium plan for Better renaming experience.

• send a photo to me to add as custom Thumbnail.

• send your files to me to rename.."""
	keybord = InlineKeyboardMarkup([[ 
        			InlineKeyboardButton("💳  ᴜᴩɢʀᴀᴅᴇ",url = "https://graph.org/Buy-05-14")], 
        			[InlineKeyboardButton("• ʙᴀᴄᴋ •",callback_data = "upgrade")  ]])
	await update.message.edit(text = text,reply_markup = keybord)
	

@Client.on_message(filters.private & filters.command(["help"]))
async def upgradecm(bot,message):
	text = """  📚 Available Commands:

➢ /start - check i'm alive 

➢ /plans - check available plan info

➢ /set_caption - To add your custom caption 

➢ /see_caption - To see your custom caption

➢ /del_caption - To delete your custom caption

➢ /viewthumb - To see your custom thumbnail

➢ /delthumb - To delete your custom thumbnail

• upgrade your premium plan for Better renaming experience.

• send a photo to me to add as custom Thumbnail.

• send your files to me to rename.."""
	keybord = InlineKeyboardMarkup([[ 
        			InlineKeyboardButton("💳  ᴜᴩɢʀᴀᴅᴇ",url = "https://graph.org/Buy-05-14")], 
        			[InlineKeyboardButton("• ʙᴀᴄᴋ •",callback_data = "upgrade")  ]])
	await message.reply_text(text = text,reply_markup = keybord)
