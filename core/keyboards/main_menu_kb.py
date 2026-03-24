from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from texts.translator import t
def main_menu_kb(event):
    kb = InlineKeyboardMarkup(inline_keyboard=[

        [InlineKeyboardButton(text=t(event, "btn_ichancy_main"), callback_data="ichancy_main")],
        [
            InlineKeyboardButton(text=t(event,"btn_deposit"), callback_data="my_wallets"),
            InlineKeyboardButton(text=t(event,"btn_withdraw"), callback_data="my_wallets"),
         
         
         ],
        [
            InlineKeyboardButton(text=t(event,"btn_present"), callback_data="my_wallets"),
            InlineKeyboardButton(text=t(event,"btn_prize"), callback_data="my_wallets"),
         
         
         ],
        [InlineKeyboardButton(text=t(event,"btn_ichancy_site"), callback_data="https://www.ichancy.com/")],
        [InlineKeyboardButton(text=t(event,"btn_referrals"), callback_data="referrals")],
        [InlineKeyboardButton(text=t(event,"btn_support"), callback_data="support")],
        [InlineKeyboardButton(text=t(event,"btn_profile"), callback_data="my_wallets")],



    ])
    return kb