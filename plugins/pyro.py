import os
from pyrogram import Client,filters
from . import *

import logging
logging.basicConfig(level=logging.INFO)

PHONE = os.environ.get("PHONE_NUMBER")
LCODE = os.environ.get("LCODE")
VPASS = os.environ.get("STEP_PASS")

Client = Client("PYROCLIENT",api_id=Var.API_ID,api_hash=Var.API_HASH,
               phone_number=PHONE,
               phone_code = LCODE,
               password = VPASS)

@Client.on_message(filters.outgoing & filters.command(["pyro"],"."))
async def ree(client,message):
  await message.reply_text("Pyrogram")
  
Client.run()
