from aiogram import types
from aiogram.dispatcher.filters import Text
from aiogram.dispatcher import Dispatcher
from aiogram.dispatcher import FSMContext
from aiogram_broadcaster import MessageBroadcaster

from ..database.database import Repo
from ..database.states import UserStatus


from ..config import ADMINS

async def cancel_cmd(message: types.Message, state: FSMContext, repo: Repo):
    current_state = await state.get_state()
    if (current_state == UserStatus.mass_mailing or current_state == UserStatus.set_money):

        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)

        button1 = types.KeyboardButton('Выдать деньги')
        button2 = types.KeyboardButton('Массовая рассылка')
        button3 = types.KeyboardButton('Выход')

        markup.add(button1).add(button2).add(button3)

        await UserStatus.admin.set()
        await message.bot.send_message(message.from_user.id, "Выберите действие", reply_markup=markup)
        
async def admin_cmd(message: types.Message, state: FSMContext, repo: Repo):
    if (message.from_user.id in ADMINS):
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        button1 = types.KeyboardButton('Выдать деньги')
        button2 = types.KeyboardButton('Массовая рассылка')
        button3 = types.KeyboardButton('Выход')

        markup.add(button1).add(button2).add(button3)

        await UserStatus.admin.set()
        print ('зашел')
        await message.bot.send_message(message.from_user.id, 'Вы вошли в режим администрирования',reply_markup=markup)
    else: 
        await message.bot.send_message(message.from_user.id, 'У вас недостаточно прав для выполнения данного действия')

async def echo_message_admin(message: types.Message, state: FSMContext, repo: Repo):
    current_state = await state.get_state()
    print(current_state)
    if (message.text == "Массовая рассылка"):

        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        button = types.KeyboardButton('Отмена')
        
        markup.add(button)
        
        await UserStatus.mass_mailing.set()
        await message.bot.send_message(message.from_user.id, "Введите сообщение", reply_markup=markup)

    elif (message.text == "Выдать деньги"):
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        button = types.KeyboardButton('Отмена')
        
        markup.add(button)
        
        await UserStatus.set_money.set()
        await message.bot.send_message(message.from_user.id, "Введите id пользователя и сумму", reply_markup=markup)

    elif (message.text == "Выход"):
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        button1 = types.KeyboardButton('Получить отчет')
        button2 = types.KeyboardButton('Личный кабинет')

        markup.add(button1).add(button2)

        await state.finish()
        print ('exit')
        await message.bot.send_message(message.from_user.id, 'Выберите действие', reply_markup=markup)


async def add_money(message: types.Message, state: FSMContext, repo: Repo):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    button1 = types.KeyboardButton('Выдать деньги')
    button2 = types.KeyboardButton('Массовая рассылка')
    button3 = types.KeyboardButton('Выход')

    markup.add(button1).add(button2).add(button3)
    await repo.set_value(int(message.text.split()[0]), int(message.text.split()[1]))
    await message.bot.send_message(message.from_user.id, "средства успешно зачислены", reply_markup=markup)
    await UserStatus.admin.set()

async def mass_mailing(message: types.Message, state: FSMContext, repo: Repo):

    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    button1 = types.KeyboardButton('Выдать деньги')
    button2 = types.KeyboardButton('Массовая рассылка')
    button3 = types.KeyboardButton('Выход')

    markup.add(button1).add(button2).add(button3)


    users = await repo.get_users()
    await MessageBroadcaster(users, message).run()
    await message.bot.send_message(message.from_user.id, "Рассылка успешно завершена", reply_markup=markup)
    await UserStatus.admin.set()







def register_admins_handlers(dp: Dispatcher):
    dp.register_message_handler(admin_cmd, commands="admin",state="*")
    print('1 registred')
    dp.register_message_handler(echo_message_admin, state=UserStatus.admin)
    print('2 registred')
    dp.register_message_handler(cancel_cmd, Text(equals="Отмена", ignore_case=True), state="*")
    print('3 registred')
    dp.register_message_handler(add_money, state=UserStatus.set_money)
    print('5 registred')
    dp.register_message_handler(mass_mailing, state=UserStatus.mass_mailing)
    print('6 registred')
