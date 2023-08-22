import asyncio
from pyrogram import Client, compose,idle
import os

from plugins.cb_data import app as Client2
from aiohttp import web

PORT = "8080"

TOKEN = os.environ.get("TOKEN", "")

API_ID = int(os.environ.get("API_ID", ""))

API_HASH = os.environ.get("API_HASH", "")

STRING = os.environ.get("STRING", "")

bot = Client(

           "Renamer",

           bot_token=TOKEN,

           api_id=API_ID,

           api_hash=API_HASH,

           plugins=dict(root='plugins'))
           

async def start(self):
        await super().start()
        me = await self.get_me()
        self.mention = me.mention
        self.username = me.username 
        self.force_channel = CHANNEL
        if CHANNEL:
            try:
                link = await self.export_chat_invite_link(CHANNEL)                  
                self.invitelink = link
            except Exception as e:
                print(e)
                print("Make Sure Bot admin in force sub channel")             
                self.force_channel = None
        app = web.AppRunner(await web_server())
        await app.setup()
        bind_address = "0.0.0.0"       
        await web.TCPSite(app, bind_address, PORT).start()     
        print(f"{me.first_name} 𝚂𝚃𝙰𝚁𝚃𝙴𝙳 ⚡️⚡️⚡️")
      

    async def stop(self, *args):
        await super().stop()      
        print("Bot Stopped")

if STRING:
    apps = [Client2,bot]
    for app in apps:
        app.start()
    idle()
    for app in apps:
        app.stop()
    
else:
    bot.run()
