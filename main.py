import asyncio
import sys
import logging

from dotenv import load_dotenv
from aiogram import Bot, Dispatcher

from app.data.config import BOT_TOKEN

from app.handlers.main_handler import router
from app.handlers.co_worker_menu import cw_router
from app.handlers.courses_menu import c_router
from app.handlers.about_menu import about_router
from app.handlers.contact_us_menu import c_u_router
from app.handlers.vacancies_menu import v_router
from app.handlers.settings_menu import settings_router

from app.utils.notify_admins import admin_router

from app.database.models import async_main

async def main():
    await async_main()
    load_dotenv()
    bot = Bot(BOT_TOKEN)
    dp = Dispatcher()
    dp.include_router(router)
    dp.include_router(cw_router)
    dp.include_router(c_router)
    dp.include_router(about_router)
    dp.include_router(c_u_router)
    dp.include_router(v_router)
    dp.include_router(settings_router)
    dp.include_router(admin_router)
    await dp.start_polling(bot)

if __name__ == '__main__':
    try:
        logging.basicConfig(level=logging.INFO, stream=sys.stdout)
        asyncio.run(main())
    except KeyboardInterrupt:
        print("Process finished.")