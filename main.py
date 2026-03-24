import asyncio
import logging
import sys
from aiogram import Bot, Dispatcher
from aiogram.fsm.storage.memory import MemoryStorage
from aiogram.types import BotCommand
from aiogram.webhook.aiohttp_server import SimpleRequestHandler, setup_application
from aiohttp import web
from aiogram.client.default import DefaultBotProperties
from core.services.ichancy_client import IchancyClient

from core.handlers import all_routers 

from config import BOT_TOKEN
from core.database.database import init_db_connection, init_db, close_db, db


WEBHOOK_URL = 0 #os.getenv("WEBHOOK_URL")  # إذا كنت تستخدم Webhook
USE_WEBHOOK = False #os.getenv("USE_WEBHOOK", "false").lower() == "true"

# استيراد الروترات

#ضبط الاوامر
async def set_bot_commands(bot: Bot):
    """إعداد أوامر البوت في تيليجرام"""
    commands = [
        BotCommand(command="start", description="تشغيل البوت"),
        BotCommand(command="account", description="حسابي"),
    ]
    await bot.set_my_commands(commands)



async def on_startup(bot: Bot):
    """تشغيل المهام عند بدء البوت"""
    await set_bot_commands(bot)
    logging.info("Bot started successfully")


def register_routers(dp: Dispatcher):
    """تسجيل جميع الروترات"""
    for router in all_routers:
        dp.include_router(router)
   


async def main():
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)

    bot = Bot(token=BOT_TOKEN, default=DefaultBotProperties(parse_mode="HTML"))
    dp = Dispatcher(storage=MemoryStorage())
    # إنشاء الاتصال مرة واحدة
    await init_db_connection()
    
    await init_db()
    dp.startup.register(on_startup)
    register_routers(dp)
    #دالة تحقق من تغير حالة طلب 

    # عند تشغيل البوت (startup)
    ichancy = IchancyClient("Yabany@agent.nsp", "Yabany@21")
    await ichancy.login()   # تسجيل الدخول مرة واحدة


    #await add_admin(OWNER_IDS, "owner")

    # تشغيل Webhook
    if USE_WEBHOOK:
        app = web.Application()
        webhook_handler = SimpleRequestHandler(dp, bot)
        webhook_handler.register(app, path="/webhook")

        setup_application(app, dp, bot=bot)

        await bot.set_webhook(WEBHOOK_URL + "/webhook")
        logging.info(f"Webhook set to: {WEBHOOK_URL}/webhook")

        web.run_app(app, host="0.0.0.0", port=8080)

    else:
        # تشغيل Polling
        try:
            await dp.start_polling(bot, skip_updates=True)
        except KeyboardInterrupt:
            print("Bot stopped manually.")
        finally:
            if db:
                await db.close()
            await bot.session.close()




if __name__ == "__main__":
    try:
        asyncio.run(main())
    except (KeyboardInterrupt, SystemExit):
        logging.info("Bot stopped")
