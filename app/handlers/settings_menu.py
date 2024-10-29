from aiogram import Router, F
from aiogram.types import CallbackQuery, Message
from aiogram.fsm.context import FSMContext

from app.states.states import Comment, MainMenu
from app.keyboards import keyboards as kb
from app.utils.internatinalition import _i18n_ as inter
from app.utils.notify_admins import notify_admin
from app.data.photo_ids import TRAMPLIN_PHOTO_ID as tramplin_logo

settings_router = Router()

@settings_router.callback_query(F.data == 'settings_menu')
async def mentors(callback : CallbackQuery):
    await callback.answer(text="Settings :")
    await callback.message.delete()
    await callback.message.answer(text="Settings :", reply_markup=await kb.get_settings(callback.from_user.id))

@settings_router.callback_query(F.data == 'comment')
async def get_comment(callback : CallbackQuery, state : FSMContext):
    await callback.answer(text="Comment : ")
    await callback.answer(text="Settings :")
    await state.set_state(Comment.description)
    await callback.message.answer(text=await inter.get_comment(callback.from_user.id))

@settings_router.message(Comment.description)
async def get_comm(message : Message, state : FSMContext):
    await notify_admin(info=f"Comment : \n{message.text}", user_id=message.from_user.id)
    await message.answer(text=await inter.get_s_comm(message.from_user.id))
    await message.answer_photo(photo=tramplin_logo, caption=await inter.get_info(message.from_user.id), reply_markup=kb.start_menu)