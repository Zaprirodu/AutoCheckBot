from aiogram.dispatcher.filters.state import StatesGroup, State


class UserStatus(StatesGroup):
    check_vin = State()

    waiting_bill = State()
    waiting_payment = State()
