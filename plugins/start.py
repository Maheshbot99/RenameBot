from datetime import date as date_
import datetime
import os
from pyrogram.errors.exceptions.bad_request_400 import UserNotParticipant
import time
from pyrogram import Client, filters
from pyrogram.types import (
    InlineKeyboardButton, InlineKeyboardMarkup)
import humanize
from helper.progress import humanbytes

from helper.database import insert, find_one, used_limit, usertype, uploadlimit, addpredata, total_rename, total_size
from pyrogram.file_id import FileId
from helper.database import daily as daily_
from helper.date import check_expi
import os

CHANNEL = os.environ.get('CHANNEL', "")
STRING = os.environ.get("STRING", "")
ADMIN = int(os.environ.get("ADMIN", 5450011131))
bot_username = os.environ.get("BOT_USERNAME","")
log_channel = int(os.environ.get("LOG_CHANNEL", "Rename4GB_Msbot"))
token = os.environ.get('TOKEN', '')
botid = token.split(':')[0]
FLOOD = 500
LAZY_PIC = os.environ.get("LAZY_PIC", "")


# Part of Day --------------------
currentTime = datetime.datetime.now()

if currentTime.hour < 12:
    wish = "❤️ GOOD MORNING  ❤️"
elif 12 <= currentTime.hour < 12:
    wish = '🤍 GOOD AFTERNOON 🤍'
else:
    wish = '💙 GOOD EVENING 💙'

# -------------------------------


@Client.on_message(filters.private & filters.command(["start"]))
async def start(client, message):
    old = insert(int(message.chat.id))
    try:
        id = message.text.split(' ')[1]
    except:
        txt=f"""ʜᴇʟʟᴏ - {message.from_user.mention} , \nɪ  ᴀᴍ  ᴀɴ  ᴀᴅᴠᴀɴᴄᴇ  ꜰɪʟᴇ  ʀᴇɴᴀᴍᴇʀ  ᴀɴᴅ  ᴄᴏɴᴠᴇʀᴛᴇʀ  ʙᴏᴛ  ᴡɪᴛʜ  ᴘᴇʀᴍᴀɴᴇɴᴛ  ᴀɴᴅ  ᴄᴜsᴛᴏᴍ  ᴛʜᴜᴍʙɴᴀɪʟ  sᴜᴘᴘᴏʀᴛ. \n\nᴊᴜsᴛ  sᴇɴᴅ  ᴍᴇ  ᴀɴʏ  ᴠɪᴅᴇᴏ  ᴏʀ ᴅᴏᴄᴜᴍᴇɴᴛ !!"""
        await message.reply_photo(photo=LAZY_PIC,
                                caption=txt,
                                reply_markup=InlineKeyboardMarkup(
                                      [[InlineKeyboardButton("ᴩʀᴇᴍɪᴜᴍ ᴩʟᴀɴꜱ",callback_data = "upgrade")],
                                      [InlineKeyboardButton("ᴄʜᴀɴɴᴇʟ", url='https://t.me/Cinema_HDHub'),
                                      InlineKeyboardButton("ᴄᴏɴᴛᴀᴄᴛ ᴜꜱ", url='https://t.me/MaHi_458')],
                                      [InlineKeyboardButton("• ʜᴇʟᴩ •",callback_data = "help")]
                                      ]))
        return
    if id:
        if old == True:
            try:
                await client.send_message(id, "Your Friend is Already Using Our Bot")
                await message.reply_photo(photo=LAZY_PIC,
                                         caption=txt,
                                         reply_markup=InlineKeyboardMarkup(
                                             [[InlineKeyboardButton("ᴩʀᴇᴍɪᴜᴍ ᴩʟᴀɴꜱ",callback_data = "upgrade")],
                                              [InlineKeyboardButton("ᴄʜᴀɴɴᴇʟ", url='https://t.me/Cinema_HDHub'),
                                             InlineKeyboardButton("ᴄᴏɴᴛᴀᴄᴛ ᴜꜱ", url='https://t.me/MaHi_458')],
                                             [InlineKeyboardButton("• ʜᴇʟᴩ •",callback_data = "help")]
                                          ]))
            except:
                return
        else:
            await client.send_message(id, "Congrats! You Won 100MB Upload limit")
            _user_ = find_one(int(id))
            limit = _user_["uploadlimit"]
            new_limit = limit + 104857600
            uploadlimit(int(id), new_limit)
            await message.reply_text(text=f"""
	ʜᴇʟʟᴏ - {message.from_user.mention} , \nɪ  ᴀᴍ  ᴀɴ  ᴀᴅᴠᴀɴᴄᴇ  ꜰɪʟᴇ  ʀᴇɴᴀᴍᴇʀ  ᴀɴᴅ  ᴄᴏɴᴠᴇʀᴛᴇʀ  ʙᴏᴛ  ᴡɪᴛʜ  ᴘᴇʀᴍᴀɴᴇɴᴛ  ᴀɴᴅ  ᴄᴜsᴛᴏᴍ  ᴛʜᴜᴍʙɴᴀɪʟ  sᴜᴘᴘᴏʀᴛ. \n\nᴊᴜsᴛ  sᴇɴᴅ  ᴍᴇ  ᴀɴʏ  ᴠɪᴅᴇᴏ  ᴏʀ ᴅᴏᴄᴜᴍᴇɴᴛ !!
	""", reply_to_message_id=message.id,
                                     reply_markup=InlineKeyboardMarkup(
                                         [[InlineKeyboardButton("ᴩʀᴇᴍɪᴜᴍ ᴩʟᴀɴꜱ",callback_data = "upgrade")],
                                          [InlineKeyboardButton("ᴄʜᴀɴɴᴇʟ", url='https://t.me/Cinema_HDHub'),
                                          InlineKeyboardButton("ᴄᴏɴᴛᴀᴄᴛ ᴜꜱ", url='https://t.me/MaHi_458')],
                                          [InlineKeyboardButton("• ʜᴇʟᴩ •",callback_data = "help")]
                                          ]))
    


@Client.on_message((filters.private & (filters.document | filters.audio | filters.video)) | filters.channel & (filters.document | filters.audio | filters.video))
async def send_doc(client, message):
    update_channel = CHANNEL
    user_id = message.from_user.id
    if update_channel:
        try:
            await client.get_chat_member(update_channel, user_id)
        except UserNotParticipant:
            _newus = find_one(message.from_user.id)
            user = _newus["usertype"]
            await message.reply_text("**__You are not subscribed my channel__** ",
                                     reply_to_message_id=message.id,
                                     reply_markup=InlineKeyboardMarkup(
                                         [[InlineKeyboardButton("❆ ᴊᴏɪɴ ᴏᴜʀ ʙᴀᴄᴋ-ᴜᴩ ᴄʜᴀɴɴᴇʟ ❆", url=f"https://t.me/{update_channel}")]]))
            await client.send_message(log_channel,f"🦋 #ReName_MsBot 🦋,\n\n**ID** : `{user_id}`\n**Name**: {message.from_user.mention} {message.from_user.last_name}\n**User-Plan** : {user}\n\n ",
                                                                                                       reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton("🔺 Restrict User ( **pm** ) 🔺", callback_data="ceasepower")]]))
            return

    try:
        bot_data = find_one(int(botid))
        prrename = bot_data['total_rename']
        prsize = bot_data['total_size']
        user_deta = find_one(user_id)
    except:
        await message.reply_text("Use About cmd first /myplan")
    try:
        used_date = user_deta["date"]
        buy_date = user_deta["prexdate"]
        daily = user_deta["daily"]
        user_type = user_deta["usertype"]
    except:
        await message.reply_text(text=f"ʜᴇʟʟᴏ {message.from_user.mention} , \n\nꜱᴏʀʀy ꜰᴏʀ ᴛʜɪꜱ ɪꜱꜱᴜᴇ \nᴡᴇ ᴀʀᴇ ᴄᴜʀʀᴇɴᴛʟy ᴡᴏʀᴋɪɴɢ ᴏɴ ᴛʜɪꜱ ɪꜱꜱᴜᴇ \nᴩʟᴇᴀꜱᴇ ʙᴜy ᴩʀᴇᴍɪᴜᴍ ᴏʀ ʀᴇꜱᴛᴀʀᴛ ʙᴏᴛ \n\nᴜꜱᴇ ᴛʜɪꜱ ᴄᴏᴍᴍᴀɴᴅ - /restart",
                                  reply_markup=InlineKeyboardMarkup([
                                                                     [InlineKeyboardButton("ᴩʀᴇᴍɪᴜᴍ ᴩʟᴀɴꜱ",callback_data = "upgrade")],
                                                                     [InlineKeyboardButton("ᴄʜᴀɴɴᴇʟ", url='https://t.me/Cinema_HDHub'),
                                                                     InlineKeyboardButton("ᴄᴏɴᴛᴀᴄᴛ ᴜꜱ", url='https://t.me/MaHi_458')],
                                                                     [InlineKeyboardButton("• ʜᴇʟᴩ •",callback_data = "help")]
                                                                    ]))
        await message.reply_text(text=f"🦋")
        return 

    c_time = time.time()

    if user_type == "Free":
        LIMIT = 600
    else:
        LIMIT = 610
    then = used_date + LIMIT
    left = round(then - c_time)
    conversion = datetime.timedelta(seconds=left)
    ltime = str(conversion)
    if left > 0:
        await message.reply_text(f"```ꜱᴏʀʀy ᴅᴜᴅᴇ ɪ ᴀᴍ ɴᴏᴛ ᴏɴʟy ꜰᴏʀ yᴏᴜ \n ꜰʟᴏᴏᴅ ᴄᴏɴᴛʀᴏʟ ɪꜱ ᴀᴄᴛɪᴠᴇ ꜱᴏ ᴩʟᴇᴀꜱᴇ ᴡᴀɪᴛ ꜰᴏʀ``` **{ltime}**", reply_to_message_id=message.id)
    else:
        # Forward a single message
        media = await client.get_messages(message.chat.id, message.id)
        file = media.document or media.video or media.audio
        dcid = FileId.decode(file.file_id).dc_id
        filename = file.file_name
        value = 2147483648
        used_ = find_one(message.from_user.id)
        used = used_["used_limit"]
        limit = used_["uploadlimit"]
        expi = daily - \
            int(time.mktime(time.strptime(str(date_.today()), '%Y-%m-%d')))
        if expi != 0:
            today = date_.today()
            pattern = '%Y-%m-%d'
            epcho = int(time.mktime(time.strptime(str(today), pattern)))
            daily_(message.from_user.id, epcho)
            used_limit(message.from_user.id, 0)
        remain = limit - used
        if remain < int(file.file_size):
            await message.reply_text(f"100% ᴏꜰ ᴅᴀɪʟy {humanbytes(limit)} ᴅᴀᴛᴀ qᴜᴏᴛᴀ ᴇxʜᴀᴜꜱᴛᴇᴅ.\n\n  ꜰɪʟᴇ ꜱɪᴢᴇ ᴅᴇᴛᴇꜱᴛᴇᴅ {humanbytes(file.file_size)}\n  ᴜꜱᴇᴅ ᴅᴀɪʟy ʟɪᴍɪᴛ {humanbytes(used)}\n\nyᴏᴜ ʜᴀᴠᴇ ᴏɴʟy **{humanbytes(remain)}** ʟᴇꜰᴛ ᴏɴ yᴏᴜʀ ᴀᴄᴄᴏᴜɴᴛ.\nɪꜰ yᴏᴜ ᴡᴀɴᴛ ᴛᴏ ʀᴇɴᴀᴍᴇ ʟᴀʀɢᴇ ꜰɪʟᴇ ᴜᴩɢʀᴀᴅᴇ yᴏᴜʀ ᴩʟᴀɴ ", reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton("💳 ᴜᴩɢʀᴀᴅᴇ", callback_data="upgrade")]]))
            return
        if value < file.file_size:
            
            if STRING:
                if buy_date == None:
                    await message.reply_text(f" **yᴏᴜ ᴄᴀɴ'ᴛ ᴜᴩʟᴏᴀᴅ ᴍᴏʀᴇ ᴛʜᴇɴ {humanbytes(limit)} ᴜꜱᴇᴅ ᴅᴀɪʟy ʟɪᴍɪᴛ** {humanbytes(used)} ", reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton("💳 ᴜᴩɢʀᴀᴅᴇ", callback_data="upgrade")]]))
                    return
                pre_check = check_expi(buy_date)
                if pre_check == True:
                    await message.reply_text(f"""**__What do you want me to do with this file?__**\n**File Name** :- {filename}\n**File Size** :- {humanize.naturalsize(file.file_size)}""", reply_to_message_id=message.id, reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton("✍  ʀᴇɴᴀᴍᴇ", callback_data="rename"), InlineKeyboardButton("✖️ ᴄᴀɴᴄᴇʟ", callback_data="cancel")]]))
                    total_rename(int(botid), prrename)
                    total_size(int(botid), prsize, file.file_size)
                else:
                    uploadlimit(message.from_user.id, 2147483648)
                    usertype(message.from_user.id, "Free")

                    await message.reply_text(f'**yᴏᴜʀ ᴩʟᴀɴ ᴇxᴩɪʀᴇᴅ ᴏɴ {buy_date}', quote=True)
                    return
            else:
                await message.reply_text("**ᴜᴩɢʀᴀᴅᴇ yᴏᴜʀ ᴩʟᴀɴ ᴛᴏ ʀᴇɴᴀᴍᴇ ꜰɪʟᴇꜱ ʟᴀʀɢᴇʀ ᴛʜᴀɴ 2ɢʙ**")
                return
        else:
            if buy_date:
                pre_check = check_expi(buy_date)
                if pre_check == False:
                    uploadlimit(message.from_user.id, 2147483648)
                    usertype(message.from_user.id, "Free")

            filesize = humanize.naturalsize(file.file_size)
            fileid = file.file_id
            total_rename(int(botid), prrename)
            total_size(int(botid), prsize, file.file_size)
            await message.reply_text(f"""**__What do you want me to do with this file?__**\n**File Name** :- {filename}\n**File Size** :- {filesize}""", reply_to_message_id=message.id, reply_markup=InlineKeyboardMarkup(
                [[InlineKeyboardButton("✍  ʀᴇɴᴀᴍᴇ", callback_data="rename"),
                  InlineKeyboardButton("✖️ ᴄᴀɴᴄᴇʟ", callback_data="cancel")]]))
