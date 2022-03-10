import asyncio
import logging

from datetime import datetime
from aiogram import Bot, types
from aiogram.dispatcher.filters import Text
from aiogram.dispatcher import Dispatcher
from aiogram.dispatcher import FSMContext

from ..database.database import Repo
from ..database.states import UserStatus


from ..gibdd import gibdd
from ..database import states

async def start_cmd(message: types.Message, repo: Repo):

    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    button1 = types.KeyboardButton('Получить отчет')
    button2 = types.KeyboardButton('Личный кабинет')
    money = types.InlineKeyboardButton('Пополнить счет', callback_data='money')

    markup.add(button1).add(button2)
    inline_kb = types.InlineKeyboardMarkup().add(money)

    await repo.add_new_user(message.from_user.id)

    balance = await repo.read_balance(message.from_user.id)
    ms = """Ваш ID: %s\nВаш баланс: %s&#8381""" % (message.from_user.id, balance)

    await message.bot.send_message(666624047, "id: %s \n first name: %s \n last name: %s \n username: %s" % (message.from_user.id, message.from_user.first_name, message.from_user.last_name, message.from_user.username))

    await message.bot.send_message(message.from_user.id, ms, reply_markup=inline_kb)
    await message.bot.send_message(message.from_user.id, 'Выберите действие', reply_markup=markup)


async def cancel_cmd(message: types.Message, state: FSMContext, repo: Repo):
    
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    button1 = types.KeyboardButton('Получить отчет')
    button2 = types.KeyboardButton('Личный кабинет')

    markup.add(button1).add(button2)
    
    current_state = await state.get_state()

    if current_state is None:
        await message.bot.send_message(message.from_user.id, 'Выберите действие', reply_markup=markup)
        return

    await state.finish()

    await message.bot.send_message(message.from_user.id, 'Выберите действие', reply_markup=markup)


def register_commands_handlers(dp: Dispatcher):
    dp.register_message_handler(start_cmd, commands="start",state="*")
    dp.register_message_handler(cancel_cmd, commands="cancel", state="*")
    dp.register_message_handler(cancel_cmd, Text(equals="отмена", ignore_case=True), state="*")