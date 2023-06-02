"""lokaman"""
from pyrogram.types import (InlineKeyboardButton, InlineKeyboardMarkup,ForceReply)
from pyrogram import Client , filters

@Client.on_callback_query(filters.regex('kingmsaa'))
async def upgrade(bot,update):
	text = """<b>❉ Hᴏᴡ Tᴏ Cᴏɴɴᴇᴄᴛ Yᴏᴜʀ Oᴡɴ Sʜᴏʀᴛɴᴇʀ</b>

<b>➥ Iғ Yᴏᴜ Wᴀɴᴛ Tᴏ Cᴏɴɴᴇᴄᴛ Yᴏᴜʀ Oᴡɴ Sʜᴏʀᴛɴᴇʀ Tʜᴇɴ Jᴜsᴛ Sᴇɴᴅ Tʜᴇ Gɪᴠᴇɴ Dᴇᴛᴀɪʟs Iɴ Cᴏʀʀᴇᴄᴛ Fᴏʀᴍᴀᴛ Iɴ  Yᴏᴜʀ Gʀᴏᴜᴘ.</b>

<b>➥ ғᴏʀᴍᴀᴛ ↓↓↓</b>
<b>/set_shortner SʜᴏʀᴛɴᴇʀSɪᴛᴇ SʜᴏʀᴛɴᴇʀAᴘɪ</b>


<b>➥ ᴇxᴀᴍᴘʟᴇ ↓↓↓</b>
<code>/set_shortner mdisklink.link 48c239abf799bfcd27ac2c26a6698e895bc6d543</code>

<b>☢ ɴᴏᴛᴇ : ʏᴏᴜ sʜᴏᴜʟᴅ ɴᴏᴛ ʙᴇ ᴀɴ ᴀɴᴏɴʏᴍᴏᴜs ᴀᴅᴍɪɴ. sᴇɴᴅ ᴄᴏᴍᴍᴀɴᴅ ᴡɪᴛʜᴏᴜᴛ ʙᴇɪɴɢ ᴀɴ ᴀɴᴏɴʏᴍᴜs ᴀᴅᴍɪɴ.</b>"""
	keybord = InlineKeyboardMarkup([[ 
        			InlineKeyboardButton('• ʙᴀᴄᴋ •', callback_data='earning')],[InlineKeyboardButton('Cʟᴏsᴇ', callback_data='close_data')  ]])
	await update.message.edit(text = text,reply_markup = keybord)
	

@Client.on_message(filters.private & filters.command(["kingmsaa"]))
async def upgradecm(bot,message):
	text = """<b>❉ Hᴏᴡ Tᴏ Cᴏɴɴᴇᴄᴛ Yᴏᴜʀ Oᴡɴ Sʜᴏʀᴛɴᴇʀ</b>

<b>➥ Iғ Yᴏᴜ Wᴀɴᴛ Tᴏ Cᴏɴɴᴇᴄᴛ Yᴏᴜʀ Oᴡɴ Sʜᴏʀᴛɴᴇʀ Tʜᴇɴ Jᴜsᴛ Sᴇɴᴅ Tʜᴇ Gɪᴠᴇɴ Dᴇᴛᴀɪʟs Iɴ Cᴏʀʀᴇᴄᴛ Fᴏʀᴍᴀᴛ Iɴ  Yᴏᴜʀ Gʀᴏᴜᴘ.</b>

<b>➥ ғᴏʀᴍᴀᴛ ↓↓↓</b>
<b>/set_shortner SʜᴏʀᴛɴᴇʀSɪᴛᴇ SʜᴏʀᴛɴᴇʀAᴘɪ</b>


<b>➥ ᴇxᴀᴍᴘʟᴇ ↓↓↓</b>
<code>/set_shortner mdisklink.link 48c239abf799bfcd27ac2c26a6698e895bc6d543</code>

<b>☢ ɴᴏᴛᴇ : ʏᴏᴜ sʜᴏᴜʟᴅ ɴᴏᴛ ʙᴇ ᴀɴ ᴀɴᴏɴʏᴍᴏᴜs ᴀᴅᴍɪɴ. sᴇɴᴅ ᴄᴏᴍᴍᴀɴᴅ ᴡɪᴛʜᴏᴜᴛ ʙᴇɪɴɢ ᴀɴ ᴀɴᴏɴʏᴍᴜs ᴀᴅᴍɪɴ.</b>"""
	keybord = InlineKeyboardMarkup([[ 
        			InlineKeyboardButton('• ʙᴀᴄᴋ •', callback_data='earning')],[InlineKeyboardButton('Cʟᴏsᴇ', callback_data='close_data')  ]])
	await message.reply_text(text = text,reply_markup = keybord)
