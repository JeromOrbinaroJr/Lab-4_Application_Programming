import asyncio
from aiogram import Bot, Dispatcher
from config import BOT_TOKEN
from handlers import commands, messages, recommend, menu

bot = Bot(token=BOT_TOKEN)
dp = Dispatcher()

commands.register_handler(dp)
messages.register_handler(dp)
recommend.register_handler(dp)
menu.register_handler(dp)

async def main():
    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)

if __name__ == '__main__':
    asyncio.run(main())