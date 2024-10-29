import logging
import time

from aiogram import Bot, Router, F
from aiogram.types import CallbackQuery, Message
from aiogram.fsm.context import FSMContext

from app.data.config import BOT_TOKEN, ADMIN
from app.keyboards import keyboards as kb
from app.states.states import AdminAnswer

bot = Bot(BOT_TOKEN)
admin_router = Router()

async def notify_admin(info, user_id):
        info += f"\n{time.strftime('%Y-%m-%d %H:%M:%S', time.localtime())}"
        try:
            await bot.send_message(chat_id=ADMIN, text=info, reply_markup=await kb.answer(user_id=user_id))

        except Exception as err:
            logging.exception(err)

@admin_router.callback_query(F.data.startswith('answer_to_'))
async def answer(callback : CallbackQuery, state : FSMContext):
    await callback.answer(text="Answer : ")
    to_user = callback.data.split('_')[2]
    await state.set_state(AdminAnswer.to_id)
    await state.update_data(to_id=to_user)

    await state.set_state(AdminAnswer.description)
    await callback.message.answer(text="Javobingizni yozing : ")

@admin_router.message(AdminAnswer.description)
async def answer_user(message : Message, state : FSMContext):
    user_id = (await state.get_data())['to_id']
    info = "Answer from admin : "
    info += f'\n{message.text}'
    await state.clear()
    try:
            await bot.send_message(chat_id=user_id, text=info)
    except Exception as err:
            logging.exception(err)