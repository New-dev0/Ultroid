import os
from pyrogram import Client,filters
from . import *
from pytgcalls import GroupCalls
import logging
logging.basicConfig(level=logging.INFO)

PYROSESSION = os.environ.get("PYROSESSION")
Client = Client(PYROSESSION,api_id=Var.API_ID,api_hash=Var.API_HASH)
pytgcalls = GroupCalls(Client)

@Client.on_message(filters.outgoing & filters.command(["pyro"],"."))
async def ree(client,message):
  await message.reply_text("Pyrogram")
  
@Client.on_message(filters.outgoing & filters.command(["join"],"."))
async def joinno(_,message):
  await pytgcalls.start(message.chat.id)
  await message.edit_text("Joined VC !!")

Client.run()
