from aiogram import Router, F
from aiogram.filters import CommandStart
from aiogram.types import Message, CallbackQuery, ReplyKeyboardRemove
from aiogram.fsm.context import FSMContext

from app.keyboards import keyboards as kb
from app.utils.internatinalition import _i18n_ as inter
from app.services.user_service import set_user
from app.states.states import MainMenu

from app.data.photo_ids import TRAMPLIN_PHOTO_ID as tramplin_logo

router = Router()

@router.message(CommandStart())
async def c_lang(message : Message):
    await set_user(message.from_user.id)
    await message.answer(text="Tilni tanlang : ", reply_markup=await kb.get_langs())

@router.callback_query(F.data == 'change_lang')
async def c_lang(callback : CallbackQuery):
    await callback.message.delete()
    await callback.message.answer(text="Tilni tanlang : ", reply_markup=await kb.get_langs())    

@router.message(F.text == 'O\'zbek')
async def cmd_start(message : Message):
    await inter.set_lang('uz', message.from_user.id)
    await message.answer(text="O'zbek tili tanlandi :", reply_markup=ReplyKeyboardRemove())
    await message.answer_photo(photo=tramplin_logo, caption=await inter.get_info(message.from_user.id), reply_markup=kb.start_menu)

@router.message(F.text == 'Русский')
async def cmd_start(message : Message):
    await inter.set_lang('ru', message.from_user.id)
    await message.answer(text="Выбран русский язык :", reply_markup=ReplyKeyboardRemove())
    await message.answer_photo(photo=tramplin_logo, caption=await inter.get_info(message.from_user.id), reply_markup=kb.start_menu)

@router.callback_query(F.data == 'to_main_menu' or MainMenu.main_menu)
async def main_menu(callback : CallbackQuery, state : FSMContext):
    await callback.answer(text="Main menu :")
    await callback.message.delete()
    await callback.message.answer_photo(photo=tramplin_logo, reply_markup=await kb.get_main_menu(callback.from_user.id))
    await state.clear()