from aiogram.fsm.state import StatesGroup, State
class CreateIchancyAccount(StatesGroup):
    waiting_username = State()
    waiting_password = State()

class DeposiIchancyAccount(StatesGroup):
    waiting_amount = State()