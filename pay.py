from datetime import datetime
from os import stat
from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.dispatcher.filters import Text
from aiogram.dispatcher import FSMContext

from database import Repo
from states import UserStatus

import qiwi

async def add_bill(msg: types.Message, state: FSMContext, repo: Repo):
    must_pay = 0
    if(msg.text == "отмена" or msg.text == "Отмена"):
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        button1 = types.KeyboardButton('Получить отчет')
        button2 = types.KeyboardButton('Личный кабинет')

        markup.add(button1).add(button2)

        await msg.bot.send_message(msg.from_user.id, 'Выберите действие', reply_markup=markup)
        await state.finish()
        return
    try:
        must_pay = int(msg.text)
    except ValueError:
        await msg.bot.send_message(msg.from_user.id, "Пожалуйста введите корректную сумму.")
        return
    if (must_pay <= 0):
        await msg.bot.send_message(msg.from_user.id, "Пожалуйста не вводите отрицательных значений.")
        return
    await UserStatus.waiting_payment.set()  
    now = datetime.now()
    dt_string = now.strftime("%d_%m_%Y_%H_%M_%S")
    billid = f"{msg.from_user.id}_{dt_string}"
    await repo.add_bills(billid, int(must_pay))
    await state.update_data(billid=billid)
    await state.update_data(pay=must_pay)

    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    button1 = types.KeyboardButton('Отмена заказа')

    markup.add(button1)

    keyboard_markup = types.InlineKeyboardMarkup()
    keyboard_markup.add(types.InlineKeyboardButton(text='Оплатил', callback_data="pay_check"))
    link = str(qiwi.get_invoice(str(billid), float(must_pay)))
    txt = f"Адрес сохранён." \
          f"Оплатите заказ на сумму {must_pay} &#8381 по ссылке ниже и нажмите после этого на кнопку: Оплатил\n\n" \
          f"{link}"
    message = await msg.answer(txt, reply_markup=keyboard_markup)
    await msg.bot.send_message(msg.from_user.id, "Вы можете отменить платеж нажав на соответствующую кнопку", reply_markup=markup)
    await state.update_data(invoice=message.message_id)


async def cancel_payment(message: types.Message, state: FSMContext, repo: Repo):
    user_data = await state.get_data()
    billid = user_data['billid']
    await repo.delete_bill(billid)
    invoice = user_data['invoice']
    
    await message.bot.delete_message(message.from_user.id, invoice)
    await message.bot.delete_message(message.from_user.id, invoice+1)

    await state.finish()

    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    button1 = types.KeyboardButton('Получить отчет')
    button2 = types.KeyboardButton('Личный кабинет')

    markup.add(button1).add(button2)

    await message.bot.send_message(message.from_user.id, 'Выберите действие', reply_markup=markup)

def register_pay(dp: Dispatcher):
    dp.register_message_handler(add_bill, state=UserStatus.waiting_bill)
    dp.register_message_handler(cancel_payment, Text(equals="отмена заказа", ignore_case=True), state=UserStatus.waiting_payment)