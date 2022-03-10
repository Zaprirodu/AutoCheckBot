import asyncpg
import asyncio
import logging

from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher import FSMContext
from postgres_middleware import DbMiddleware
from throttling import ThrottlingMiddleware

import pay
import payment
import commands_handlers
import text_handlers

from states import UserStatus
from config import TOKEN

import config
import database


logger = logging.getLogger(__name__)

async def main():
    
    logging.basicConfig(level=logging.INFO)
    storage = MemoryStorage()
    
    bot = Bot(token=TOKEN, parse_mode=types.ParseMode.HTML)
    dp = Dispatcher(bot, storage=storage)


    pool = await asyncpg.create_pool(
        host=config.PG_HOST,
        port='5432',
        user=config.PG_USER,
        database=config.PG_DATABASE,
        password=config.PG_PASSWORD,
        command_timeout=60
    )


    dp.middleware.setup(DbMiddleware(pool))
    dp.middleware.setup(ThrottlingMiddleware())

    pay.register_pay(dp)
    commands_handlers.register_commands_handlers(dp)
    text_handlers.register_text_handlers(dp)
    payment.register_payment(dp)

    try:
        await dp.start_polling()
    finally:
        await bot.close()


if __name__ == '__main__':
    asyncio.run(main())
