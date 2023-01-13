from email.policy import default
from aiogram.dispatcher.filters.state import StatesGroup, State


class UserStatus(StatesGroup):
    default = State()

    check_vin = State()

    waiting_bill = State()
    waiting_payment = State()
    
    mass_mailing = State()
    choosing_cat = State()

    
    admin = State()
    mass_mailing = State()
    set_money = State()
