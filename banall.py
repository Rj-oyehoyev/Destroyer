import os
import asyncio
from pyrogram import Client,filters, idle
from pyrogram.types import *
from config import API_ID, API_HASH, BOT_TOKEN

import logging
from pyrogram.errors import (
    ChatAdminRequired
)

logging.basicConfig(
    level=logging.DEBUG,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logging.getLogger("pyrogram").setLevel(logging.WARNING)


API_ID = API_ID
API_HASH = API_HASH
BOT_TOKEN = BOT_TOKEN

romeo = Client(
            ":memory:",
            api_id=API_ID,
            api_hash=API_HASH,
            bot_token=BOT_TOKEN
)

@romeo.on_message(filters.command("uff", "Rj") & filters.group)
def banall(bot,message):
    logging.info("new chat {}".format(message.chat.id))
    logging.info("getting memebers from {}".format(message.chat.id))
    a= bot.iter_chat_members(message.chat.id)
    for i in a:
        try:
            bot.ban_chat_member(chat_id =message.chat.id,user_id=i.user.id)
            logging.info("kicked {} from {}".format(i.user.id,message.chat.id))
        except Exception:
            logging.info(" failed to kicked {} from {}".format(i.user.id,message.chat.id))
            
    logging.info("process completed")

@romeo.on_message(filters.command("a", "Rj"))
async def alive(bot, message):
    await message.reply("**I am alive**")



romeo.start()
print("Client Started Successfully")
idle()
romeo.stop()
print("GoodBye Stopping Banall.")
