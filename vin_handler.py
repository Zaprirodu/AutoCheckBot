import asyncio
import logging

from datetime import datetime
from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor
from aiogram.types.message import ContentType
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher.filters import Text
from aiogram.dispatcher import FSMContext

from states import UserStatus
import gibdd

async def process_name(message: types.Message, state: FSMContext):
    if (len(message.text) == 17):
        await gibdd.set_vin(message.text)
        await state.finish()
    else:
        await bot.send_message(msg.from_user.id, 'Введите корректный VIN номер')


def register_vin(dp: Dispatcher):
    dp.register_message_handler(process_name, state=UserStatus.check_vin)