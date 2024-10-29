from aiogram import Router, F
from aiogram.types import CallbackQuery
from aiogram.fsm.context import FSMContext

from app.keyboards import keyboards as kb

about_router = Router()

@about_router.callback_query(F.data == 'about_menu')
async def mentors(callback : CallbackQuery, state : FSMContext):
    await callback.answer(text="About us :")
    await callback.message.delete()
    msg = "Trampli IT academy : \nSenior darajadagi ustozlar👨🏻‍💻\nBo’lib to’lash imkoniyati💸\nAmaliyotga asoslangan darslar💡\nKuchli networking🔥\nMurojaat uchun: +998 71 113 81 88"
    await callback.message.answer(text=msg, reply_markup=await kb.get_about_us(callback.from_user.id))
