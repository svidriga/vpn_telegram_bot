import asyncio

from aiogram import Bot, Dispatcher
from aiogram.enums import ParseMode
from aiogram.fsm.storage.memory import MemoryStorage
from aiogram.client.default import DefaultBotProperties

from Bot.routers.routers import setup_routers

import os
from dotenv import load_dotenv

load_dotenv()
API_TOKEN = os.getenv('API_TOKEN')


bot = Bot(token=API_TOKEN, default=DefaultBotProperties(parse_mode=ParseMode.HTML))
dp = Dispatcher(storage=MemoryStorage())
dp.include_router(setup_routers())



async def main():
    await dp.start_polling(bot)

if __name__ == '__main__':
    asyncio.run(main())