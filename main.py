
from aiogram import Bot, Dispatcher
import asyncio
from config import BOT_TOKEN
from handlers import register_handlers


async def main():
    bot = Bot(token=BOT_TOKEN)
    dp = Dispatcher()
    await register_handlers(dp)

    print("Бот запущен...")
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())