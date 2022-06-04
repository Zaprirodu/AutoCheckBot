from pkgutil import get_data
from aiogram import types
from aiogram.dispatcher import Dispatcher
from aiogram.dispatcher.filters import Text
from aiogram.dispatcher import FSMContext


from ..database.states import UserStatus
from ..database.database import Repo


async def choose_category(call: types.CallbackQuery, repo: Repo, state: FSMContext):

    await UserStatus.choosing_cat.set()
    await call.bot.answer_callback_query(call.id)
    cats = await repo.get_category(call.from_user.id)

    await state.update_data(history = cats['history_key'])
    await state.update_data(dtp = cats['dtp_key'])
    await state.update_data(wanted = cats['wanted_key'])
    await state.update_data(restrict = cats['restrict_key'])
    await state.update_data(diagnostic = cats['diagnostic_key'])

    inline_kb = await Get_keyboard(state)
    await call.bot.send_message(call.from_user.id, "Выберите категории", reply_markup=inline_kb)

async def change_history(call: types.CallbackQuery, state: FSMContext):
    await call.bot.answer_callback_query(call.id)
    data = await state.get_data()
    await state.update_data(history = not data['history'])
    keyboard = await Get_keyboard(state)
    await call.message.edit_text(text='Выберите категории', reply_markup = keyboard)

async def change_dtp(call: types.CallbackQuery, state: FSMContext):
    await call.bot.answer_callback_query(call.id)
    data = await state.get_data()
    await state.update_data(dtp = not data['dtp'])
    keyboard = await Get_keyboard(state)
    await call.message.edit_text(text='Выберите категории', reply_markup = keyboard)

async def change_wanted(call: types.CallbackQuery, state: FSMContext):
    await call.bot.answer_callback_query(call.id)
    data = await state.get_data()
    await state.update_data(wanted = not data['wanted'])
    keyboard = await Get_keyboard(state)
    await call.message.edit_text(text='Выберите категории', reply_markup = keyboard)

async def change_restrict(call: types.CallbackQuery, state: FSMContext):
    await call.bot.answer_callback_query(call.id)
    data = await state.get_data()
    await state.update_data(restrict = not data['restrict'])
    keyboard = await Get_keyboard(state)
    await call.message.edit_text(text='Выберите категории', reply_markup = keyboard)

async def change_diagnostic(call: types.CallbackQuery, state: FSMContext):
    await call.bot.answer_callback_query(call.id)
    data = await state.get_data()
    await state.update_data(diagnostic = not data['diagnostic'])
    keyboard = await Get_keyboard(state)
    await call.message.edit_text(text='Выберите категории', reply_markup = keyboard)


async def Get_keyboard(state: FSMContext):
    user_cats = await state.get_data()

    history_key = types.InlineKeyboardButton("История %s" % check(user_cats['history']), callback_data='history')
    dtp_key = types.InlineKeyboardButton("ДТП %s" % check(user_cats['dtp']), callback_data='dtp')
    wanted_key = types.InlineKeyboardButton("Розыск %s" % check(user_cats['wanted']), callback_data='wanted')
    restrict_key = types.InlineKeyboardButton("Ограничения %s" % check(user_cats['restrict']), callback_data='restrict')
    diagnostic_key = types.InlineKeyboardButton("Диагностика %s" % check(user_cats['diagnostic']), callback_data='diagnostic')
    save_changes = types.InlineKeyboardButton("Сохранить изменения" , callback_data='save_changes')

    inline_kb = types.InlineKeyboardMarkup().add(history_key).add(dtp_key).add(wanted_key).add(restrict_key).add(diagnostic_key).add(save_changes)

    return inline_kb

async def save_changes(call: types.CallbackQuery, state: FSMContext, repo: Repo):
    saved_cats = await state.get_data()
    base_cats = await repo.get_category(call.from_user.id)

    if saved_cats['history'] != base_cats['history_key']: await repo.update_category('history_key', call.from_user.id)
    if saved_cats['dtp'] != base_cats['dtp_key']: await repo.update_category('dtp_key', call.from_user.id)
    if saved_cats['wanted'] != base_cats['wanted_key']: await repo.update_category('wanted_key', call.from_user.id)
    if saved_cats['restrict'] != base_cats['restrict_key']: await repo.update_category('restrict_key', call.from_user.id)
    if saved_cats['diagnostic'] != base_cats['diagnostic_key']: await repo.update_category('diagnostic_key', call.from_user.id)

    await state.finish()

    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    button1 = types.KeyboardButton('Получить отчет')
    button2 = types.KeyboardButton('Личный кабинет')

    markup.add(button1).add(button2)
    await call.message.delete()
    await call.bot.send_message(call.from_user.id, "Изменения сохранены", reply_markup=markup)

def check(arg: bool):
    if (arg):
        return '✅'
    else: 
        return '❎'

def register_categories(dp: Dispatcher):
    dp.register_callback_query_handler(choose_category, Text(equals="categories"), state="*")
    dp.register_callback_query_handler(change_history, Text(equals="history"), state=UserStatus.choosing_cat)
    dp.register_callback_query_handler(change_dtp, Text(equals="dtp"), state=UserStatus.choosing_cat)
    dp.register_callback_query_handler(change_wanted, Text(equals="wanted"), state=UserStatus.choosing_cat)
    dp.register_callback_query_handler(change_restrict, Text(equals="restrict"), state=UserStatus.choosing_cat)
    dp.register_callback_query_handler(change_diagnostic, Text(equals="diagnostic"), state=UserStatus.choosing_cat)
    dp.register_callback_query_handler(save_changes, Text(equals="save_changes"), state=UserStatus.choosing_cat)