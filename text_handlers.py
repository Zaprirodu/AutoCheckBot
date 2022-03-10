import asyncio
import logging
import re
import traceback

from datetime import datetime
from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.dispatcher import FSMContext

from states import UserStatus
from database import Repo

import tgraph
import states

async def check_vin(message: types.Message, repo: Repo, state: FSMContext):

    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    button1 = types.KeyboardButton('Получить отчет')
    button2 = types.KeyboardButton('Личный кабинет')

    markup.add(button1).add(button2)

    if (len(message.text) == 17):
        #try:
        await message.bot.send_message(message.from_user.id, "Пожалуйста подождите, отчет на подходе.")
        url = await tgraph.createReport(message.text)
        #except TypeError:
        #    await message.bot.send_message(message.from_user.id, "Такого VIN номера не существует. Пожалуйста введите корректный номер.")
        #except KeyError:
        #    await message.bot.send_message(message.from_user.id, "Такого VIN номера не существует. Пожалуйста введите корректный номер.")
        #else: 
        await state.finish()
        await message.bot.send_message(message.from_user.id, url, reply_markup=markup)
        await repo.set_value(message.from_user.id, -50)

    elif (len(message.text) == 8 or len(message.text) == 9):
        pattern = re.compile('[А-я][0-9]{3}[А-я]{2}[0-9]{2,3}')
        if(pattern.match(message.text)):
            try:
                await message.bot.send_message(message.from_user.id, "Пожалуйста подождите, отчет на подходе.")
                url = await tgraph.createVIN(message.text)
            except:
                await message.bot.send_message(message.from_user.id, "Такого номера не существует. Пожалуйста введите корректный номер.")
                print(traceback.format_exc())
            else:
                await state.finish()
                await message.bot.send_message(message.from_user.id, url, reply_markup=markup)
                await repo.set_value(message.from_user.id, -50)
        else:
            await message.bot.send_message(message.from_user.id, "Такого номера не существует. Пожалуйста введите корректный номер.")
    else:
        await message.bot.send_message(message.from_user.id, "Такого номера не существует. Пожалуйста введите корректный номер.")


async def echo_message(msg: types.Message, repo: Repo):
    if (msg.text == "Получить отчет" or msg.text == "получить отчет"):
        money = await repo.read_balance(msg.from_user.id)
        if money < 50:
            mes = "На вашем счете недостаточно средств для выполнения операции."
            await msg.bot.send_message(msg.from_user.id, mes)
        else:
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            button1 = types.KeyboardButton('Отмена')
            button2 = types.KeyboardButton('Личный кабинет')

            markup.add(button1).add(button2)

            await msg.bot.send_message(msg.from_user.id, "Введите VIN номер автомобили или государственный номер в формате A000AA000", reply_markup=markup)
            await UserStatus.check_vin.set()

    elif (msg.text == "Личный кабинет" or msg.text == "личный кабинет"):

        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        button = types.KeyboardButton('Получить отчет')

        markup.add(button)

        balance = await repo.read_balance(msg.from_user.id)
        ms = """Ваш ID: %s\nВаш баланс: %s&#8381""" % (msg.from_user.id, balance)
        money = types.InlineKeyboardButton('Пополнить счет', callback_data='money')
        inline_kb = types.InlineKeyboardMarkup().add(money)
        await msg.bot.send_message(msg.from_user.id, ms, reply_markup=inline_kb)
        await msg.bot.send_message(msg.from_user.id, "Выберите действие", reply_markup=markup)

    if msg.text.split(' ')[0] == "add_value":
        if (msg.from_user.id == 666624047):
            await repo.set_value(int(msg.text.split()[1]), int(msg.text.split()[2]))

def register_text_handlers(dp: Dispatcher):
    dp.register_message_handler(check_vin, state=UserStatus.check_vin)
    dp.register_message_handler(echo_message, state="*")
    