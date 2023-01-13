import re
import traceback
from unicodedata import category

from aiogram import types
from aiogram.dispatcher import Dispatcher
from aiogram.dispatcher import FSMContext
from aiogram_broadcaster import MessageBroadcaster

from ..database.states import UserStatus
from ..database.database import Repo

from ..utils import tgraph
from ..config import ADMINS

async def check_vin(message: types.Message, repo: Repo, state: FSMContext):

    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    button1 = types.KeyboardButton('Получить отчет')
    button2 = types.KeyboardButton('Личный кабинет')

    markup.add(button1).add(button2)
    if (len(message.text) == 17):
        try:
            await message.bot.send_message(message.from_user.id, "Пожалуйста подождите, отчет на подходе.")
            url = await tgraph.createReport(message.text)
        except TypeError as er:
            await message.bot.send_message(message.from_user.id, "Такого VIN номера не существует. Пожалуйста введите корректный номер.")
            print('Ошибка:\n', traceback.format_exc())
        except KeyError as er:
            await message.bot.send_message(message.from_user.id, "Такого VIN номера не существует. Пожалуйста введите корректный номер.")
            print('Ошибка:\n', traceback.format_exc())
        except ValueError as er:
            await message.bot.send_message(message.from_user.id, "Такого VIN номера не существует. Пожалуйста введите корректный номер.")
            print('Ошибка:\n', traceback.format_exc())
        else: 
            await state.finish()
            await message.bot.send_message(message.from_user.id, url, reply_markup=markup)
            await repo.set_value(message.from_user.id, -50)
            
    elif (len(message.text) == 8 or len(message.text) == 9):
        pattern = re.compile('[А-я][0-9]{3}[А-я]{2}[0-9]{2,3}')
        if(pattern.match(message.text)):
            try:
                await message.bot.send_message(message.from_user.id, "Пожалуйста подождите, отчет на подходе.")
                url = await tgraph.createReport(message.text)
            except:
                await message.bot.send_message(message.from_user.id, "Такого номера не существует. Пожалуйста введите корректный номер.")
                print(traceback.format_exc())
            else:
                await state.finish()
                await message.bot.send_message(message.from_user.id, url, reply_markup=markup)
                await repo.set_value(message.from_user.id, -50)
        else:
            await message.bot.send_message(message.from_user.id, "Такого номера не существует. Пожалуйста введите корректный номер.")

    elif (message.text == "Отмена" or message.text == "отмена"):
        print("фывы")
        await state.finish()
        await message.bot.send_message(message.from_user.id, 'Выберите действие', reply_markup=markup)
        
    else:
        await message.bot.send_message(message.from_user.id, "Такого номера не существует. Пожалуйста введите корректный номер.")


async def echo_message(msg: types.Message, repo: Repo, state: FSMContext):
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

        categories = types.InlineKeyboardButton('Выбрать категории', callback_data='categories')
        inline_kb = types.InlineKeyboardMarkup().add(money).add(categories)
        await msg.bot.send_message(msg.from_user.id, ms, reply_markup=inline_kb)
        await msg.bot.send_message(msg.from_user.id, "Выберите действие", reply_markup=markup)
    
    elif (msg.text == "Массовая рассылка" or msg.text == "массовая рассылка"):

        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        button = types.KeyboardButton('Отмена')

        markup.add(button)

        await UserStatus.mass_mailing.set()
        await msg.bot.send_message(msg.from_user.id, "Введите сообщение", reply_markup=markup)

   
    
def register_text_handlers(dp: Dispatcher):
    dp.register_message_handler(check_vin, state=UserStatus.check_vin)
    dp.register_message_handler(echo_message, state="*")
