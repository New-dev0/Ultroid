import os
from pyrogram import Client,filters
from . import *

import logging
logging.basicConfig(level=logging.INFO)

PYROSESSION = os.environ.get("PYROSESSION")

Client = Client(PYROSESSION,api_id=Var.API_ID,api_hash=Var.API_HASH)

@Client.on_message(filters.outgoing & filters.command(["pyro"],"."))
async def ree(client,message):
  await message.reply_text("Pyrogram")
  
Client.run()
