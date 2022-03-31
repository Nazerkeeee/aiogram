import asyncio
from aiogram import Bot, Dispatcher, executor
from aiogram.types import Message

my_id = 730053486
TOKEN = "1932873930:AAFAlpFzzXzNU-1cAe-eBIpsHhf6PYI5z9o"

loop = asyncio.get_event_loop()
bot = Bot(TOKEN, parse_mode="HTML")
dp = Dispatcher(bot, loop = loop)

@dp.message_handler()
async def echo(message: Message):
    if message.text == "":
        await bot.send_message(chat_id=message.from_user.id, text="Hello. This is  ")
    elif message.text == "?":
        await bot.send_message(chat_id= message.from_user.id, text="?")
    elif message.text == "":
        await bot.send_message(chat_id= message.from_user.id, text="")
    elif message.text == "":
        await bot.send_message(chat_id= message.from_user.id, text="")
    else:
        await bot.send_message(chat_id=message.from_user.id, text= "")

async def sent_to_admin(dp):
    await bot.send_message(chat_id=my_id, text="")

if __name__ == "__main__":
    executor.start_polling(dp, on_startup=sent_to_admin)