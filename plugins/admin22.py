from pyrogram.types import (
    InlineKeyboardButton, InlineKeyboardMarkup, ForceReply)
import os
from pyrogram import Client, filters
from helper.date import add_date
from helper.database import uploadlimit, usertype, addpre
ADMIN = int(os.environ.get("ADMIN", 1484670284))
log_channel = int(os.environ.get("LOG_CHANNEL", ""))


@Client.on_message(filters.private & filters.user(ADMIN) & filters.command(["warn"]))
async def warn(c, m):
        if len(m.command) >= 3:
            try:
                user_id = m.text.split(' ', 2)[1]
                reason = m.text.split(' ', 2)[2]
                await m.reply_text("User Notfied Sucessfully")
                await c.send_message(chat_id=int(user_id), text=reason)
            except:
                 await m.reply_text("User Not Notfied Sucessfully 😔")


@Client.on_message(filters.private & filters.user(ADMIN) & filters.command(["addpremium"]))
async def buypremium(bot, message):
	await message.reply_text("⊚ ꜱᴇʟᴇᴄᴛ ᴩʟᴀɴ ᴛᴏ ᴜᴩɢʀᴀᴅᴇ...", quote=True, reply_markup=InlineKeyboardMarkup([
		           [
				   InlineKeyboardButton("🥈 ꜱɪʟᴠᴇʀ", callback_data="vip1")
				   ], [
					InlineKeyboardButton("🏆 ɢᴏʟᴅ", callback_data="vip2")
				   ], [
					InlineKeyboardButton("💎 ᴅɪᴀᴍᴏɴᴅ", callback_data="vip3")
					]]))

