from pyrogram.types import (
    InlineKeyboardButton, InlineKeyboardMarkup, ForceReply)
import os
from pyrogram import Client, filters
from helper.date import add_date
from helper.database import uploadlimit, usertype, addpre
ADMIN = int(os.environ.get("ADMIN", 1484670284))


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

