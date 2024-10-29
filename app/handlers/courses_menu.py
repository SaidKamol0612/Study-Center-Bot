import os

from aiogram import Router, F, Bot
from aiogram.types import CallbackQuery
from aiogram.fsm.context import FSMContext

from app.states.states import MainMenu
from app.keyboards import keyboards as kb
from app.utils.internatinalition import _i18n_ as inter
from app.data.photo_ids import COURSES_MENU_PHOTO
from app.services import course_service as c_u

c_router = Router()

courses = {
    'backend' : ['BAACAgIAAxkBAAICzmcaglhi0AXeDJCka0EHRQRxGNphAAKXXQACzuDRSNFMW7iRQsE6NgQ', 0],
    'frontend' : ['BAACAgIAAxkBAAICzmcaglhi0AXeDJCka0EHRQRxGNphAAKXXQACzuDRSNFMW7iRQsE6NgQ', 1],
    'cyber_security' : ['BAACAgIAAxkBAAICzmcaglhi0AXeDJCka0EHRQRxGNphAAKXXQACzuDRSNFMW7iRQsE6NgQ', 2], 
    'graphic_design' : ['BAACAgIAAxkBAAICzmcaglhi0AXeDJCka0EHRQRxGNphAAKXXQACzuDRSNFMW7iRQsE6NgQ', 3]
}

@c_router.callback_query(F.data == 'courses_menu')
async def co_workers(callback : CallbackQuery, state : FSMContext):
    await callback.answer(text="Courses :")
    await callback.message.delete()
    await callback.message.answer_photo(photo=COURSES_MENU_PHOTO, reply_markup=await kb.get_courses(callback.from_user.id))
    await state.set_state(MainMenu.courses_menu)

@c_router.callback_query(MainMenu.courses_menu)
async def co_workers(callback : CallbackQuery, state : FSMContext):
    course = callback.data
    await callback.answer(text=course.title())
    await callback.message.delete()

    course_vid = courses[course][0]
    course_info = list(await inter.get_courses_info(callback.from_user.id))[courses[course][1]]
    c_url = await c_u.get_url(course)
    await callback.message.answer_video(video=course_vid, caption=course_info, reply_markup=await kb.get_course(callback.from_user.id, c_url=c_url, c_name=course))
    await state.clear()