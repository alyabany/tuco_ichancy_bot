from aiogram.types import CallbackQuery, Message
from aiogram import Router, F

from core.database.users_db import add_user
from core.keyboards.main_menu_kb import main_menu_kb
from texts.translator import t
from core.utils.hepler import now_str
router = Router()

@router.message(F.text =="/start")
async def start_handler(m: Message):
    user_id = m.from_user.id
    user_name = f"@{m.from_user.username}"
    full_name = m.from_user.full_name
    join_date = now_str()
    is_new = await add_user(user_id, user_name, full_name, join_date, None)
    if is_new:
        m.answer("انت مستخدم جديد")
    await m.answer(t(user_id, "welcome"), reply_markup=main_menu_kb(m))