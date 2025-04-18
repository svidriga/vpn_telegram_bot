import asyncio

from aiogram import Bot, Dispatcher
from aiogram.enums import ParseMode
from aiogram.fsm.storage.memory import MemoryStorage 
from aiogram.client.default import DefaultBotProperties

from Bot.routers.routers import setup_routers
from Bot.main.bot import bot

import os
from dotenv import load_dotenv

load_dotenv()
API_TOKEN = os.getenv('API_TOKEN')

dp = Dispatcher(storage=MemoryStorage())
dp.include_router(setup_routers())

async def main():
    await dp.start_polling(bot, skip_updates=True)

if __name__ == '__main__':
    asyncio.run(main())