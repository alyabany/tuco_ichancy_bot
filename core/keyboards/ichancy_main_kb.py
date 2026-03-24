from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from texts.translator import t
def ichancy_main_kb(event):
    kb = InlineKeyboardMarkup(inline_keyboard=[
        [
            InlineKeyboardButton(text=t(event, "btn_create_account"), callback_data="create_account"),
        
        ],
        [
            InlineKeyboardButton(text=t(event, "btn_recharge_account"), callback_data="recharge_account"),
            InlineKeyboardButton(text=t(event, "btn_withdraw_account"), callback_data="withdraw_account"),
            
        ]

    ])
    return kb

def ichancy_main_have_account(event):
    kb = InlineKeyboardMarkup(inline_keyboard=[
        [
            InlineKeyboardButton(text=t(event, "btn_delete_account"), callback_data="delete_account"),
        
        ],

        [
            InlineKeyboardButton(text=t(event, "btn_recharge_account"), callback_data="recharge_account"),
            InlineKeyboardButton(text=t(event, "btn_withdraw_account"), callback_data="withdraw_account"),

        ]

    ])
    return kb