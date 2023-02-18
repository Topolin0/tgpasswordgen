######################################################
##########MADE W LOVE BY @krustycrack ON TG###########
######################################################

import pyrogram
import string
import random
import tgcrypto

from pyrogram import Client, filters
from pyrogram.types import Message
from pyrogram import enums

api_id = <id> # u can find it on https://my.telegram.org/ (remove the <id>, just put the id)
api_hash = "" # u can find it on https://my.telegram.org/
bot_token = "" # obv ur bot token

app = Client(
    "my_bot",
    api_id=api_id, api_hash=api_hash,
    bot_token=bot_token
)

def password_generator(size, chars=string.ascii_letters + string.digits + string.punctuation):
    return ''.join(random.choice(chars) for _ in range(size))

@app.on_message(filters.command("start"))
async def start(_, message: Message):
    await message.reply_text("**Hi** " + message.from_user.mention + " 👋" + "\n**I can generate random secure password, you just need to write the number of characters! (Max 256 characters)**" + "\n<i>You can find my source code on https://github.com/Topolin0</i>")


@app.on_message(filters.text & filters.private)
async def gen(client, message):
    if message.text.isdigit():
        if int(message.text) > 256 or int(message.text) < 1:
            await message.reply_text("Please enter a number between 1-256!")
            return
        await message.reply_text(password_generator(int(message.text)), parse_mode=enums.ParseMode.DISABLED)
    else:
        await message.reply_text("Please enter a valid number!")

app.run()


