import os
from pyrogram import Client,filters
from . import *
from pytgcalls import GroupCall
import logging
logging.basicConfig(level=logging.INFO)

PYROSESSION = os.environ.get("PYROSESSION")
Client = Client(PYROSESSION,api_id=Var.API_ID,api_hash=Var.API_HASH)
pytgcalls = GroupCall(Client)

@Client.on_message(filters.outgoing & filters.command(["pyro"],"."))
async def ree(client,message):
  await message.reply_text("Pyrogram")
  
@Client.on_message(filters.outgoing & filters.command(["join"],"."))
async def joinno(_,message):
  await pytgcalls.start(message.chat.id)
  await message.edit_text("Joined VC !!")

@Client.on_message(filters.outgoing & filters.command("play"))
async def hhh(_,message):
  art = message.text.split(" ",maxsplit=1)[1]
  await pytgcalls.start(message.chat.id,art)
  await message.edit_text("Playing...")


Client.run()
