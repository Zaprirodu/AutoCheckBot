from datetime import datetime
from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.dispatcher.filters import Text
from aiogram.dispatcher import FSMContext

from database import Repo
from states import UserStatus

import qiwi

async def check_payment(call: types.CallbackQuery, state: FSMContext, repo: Repo):
    await call.bot.answer_callback_query(call.id)
    user_data = await state.get_data()
    billid = user_data['billid']

    if qiwi.is_bill_paid(billid):
        await call.message.answer("Ваш счет успешно пополнен!")

        await repo.update_bill_pay(billid)
        b = await repo.read_bill_amount(billid)
        await repo.set_value(call.from_user.id, b)
        await state.finish()
        await call.message.delete()

        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        button1 = types.KeyboardButton('Получить отчет')
        button2 = types.KeyboardButton('Личный кабинет')

        markup.add(button1).add(button2)

        await call.bot.send_message(call.from_user.id, "Выберите действие", reply_markup=markup)


    else:
        await call.message.answer("Счёт не оплачен! Попробуйте ещё раз...")
    await call.answer()

async def choose_sum(call: types.CallbackQuery):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    button1 = types.KeyboardButton('Отмена')

    markup.add(button1)

    await UserStatus.waiting_bill.set()
    
    await call.bot.answer_callback_query(call.id)
    await call.bot.send_message(call.from_user.id,'Введите сумму платежа', reply_markup=markup)


async def choose_sum_repeat(call: types.CallbackQuery, state: FSMContext):
    user_data = await state.get_data()
    must_pay = user_data['pay']
    message = f"У вас имеется неоплаченный счет на сумму {must_pay} &#8381, пожалуйста оплатите его, либо отмените прежде чем мы могли бы выставить вам новый счет."
    await call.bot.answer_callback_query(call.id)
    await call.bot.send_message(call.from_user.id, message)


def register_payment(dp: Dispatcher):
    dp.register_callback_query_handler(check_payment, Text(equals="pay_check"), state="*")
    dp.register_callback_query_handler(choose_sum_repeat, Text(equals="money"), state=UserStatus.waiting_payment)
    dp.register_callback_query_handler(choose_sum, Text(equals="money"), state="*")
    