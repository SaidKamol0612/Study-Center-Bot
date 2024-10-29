from aiogram.types import InlineKeyboardMarkup, ReplyKeyboardMarkup, InlineKeyboardButton, KeyboardButton
from aiogram.utils.keyboard import InlineKeyboardBuilder, ReplyKeyboardBuilder

from app.database import requests as rq
from app.utils.internatinalition import _i18n_ as inter
from app.data.config import ADMIN_PROFILE

start_menu = InlineKeyboardMarkup(inline_keyboard=[[InlineKeyboardButton(text="Menu", callback_data='to_main_menu')]])

async def get_langs():
    return ReplyKeyboardMarkup(keyboard=[[KeyboardButton(text="O'zbek"), KeyboardButton(text="Русский")]], resize_keyboard=True)

async def get_main_menu(id):
    texts = await inter.get_main_menu(id)

    main_menu = InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text=texts[0], callback_data='co_worker_menu'), InlineKeyboardButton(text=texts[1], callback_data='courses_menu')],
        [InlineKeyboardButton(text=texts[2], callback_data='about_menu')],
        [InlineKeyboardButton(text=texts[3], callback_data='vacancies_menu'), InlineKeyboardButton(text=texts[4], callback_data='contact_us_menu')],
        [InlineKeyboardButton(text=texts[5], callback_data='settings_menu')]
    ])

    return main_menu

async def get_co_workers(id):
    co_workers = InlineKeyboardBuilder()

    if co_workers != None:
        for cw in (await rq.get_co_workers()):
            co_workers.add(InlineKeyboardButton(text=f"{cw.firstname} {cw.lastname}", callback_data=f"co_worker_{cw.id}")).adjust(2)

    co_workers.row(InlineKeyboardButton(text=await inter.get_back(id), callback_data='to_main_menu'))

    return co_workers.as_markup()

async def get_courses(id):
    course_names = await inter.get_courses(id)

    courses = InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text=course_names[0], callback_data='frontend'), InlineKeyboardButton(text=course_names[1], callback_data='backend')],
        [InlineKeyboardButton(text=course_names[2], callback_data='cyber_security'), InlineKeyboardButton(text=course_names[3], callback_data='graphic_design')],
        [InlineKeyboardButton(text=course_names[4], callback_data='to_main_menu')],
    ])

    return courses

async def get_about_us(id):
    back = await inter.get_back(id)
    contact_us = await inter.get_contact_us(id)

    about_us = InlineKeyboardBuilder()

    about_us.row(InlineKeyboardButton(text=contact_us, callback_data='register_user_to_contact'))
    about_us.row(InlineKeyboardButton(text=back, callback_data='to_main_menu'))

    return about_us.as_markup()

async def get_vacancy(id, v_id):
    vacancies = InlineKeyboardBuilder()

    vacancies.add(InlineKeyboardButton(text=await inter.get_contact_us(id), callback_data=f'register_user_to_vacancy_{v_id}'))

    return vacancies.as_markup()

async def get_contact_us(id):
    contact_us = InlineKeyboardBuilder()

    contact_us.add(InlineKeyboardButton(text=await inter.get_back(id), callback_data='to_main_menu'))

    return contact_us.as_markup()

async def get_co_worker_menu(co_worker, id):
    menu = InlineKeyboardBuilder()

    menu.add(InlineKeyboardButton(text=await inter.get_contact_us(id), url=co_worker.link_contact))
    menu.add(InlineKeyboardButton(text=await inter.get_back(id), callback_data="co_worker_menu"))

    return menu.as_markup()

async def get_settings(id):
    settings_s = await inter.get_settings(id)

    settings = InlineKeyboardBuilder()

    settings.row(InlineKeyboardButton(text=settings_s[0], callback_data='change_lang'), InlineKeyboardButton(text=settings_s[1], callback_data='comment'))
    settings.row(InlineKeyboardButton(text=await inter.get_back(id), callback_data='to_main_menu'))

    return settings.as_markup()

async def get_course(id, c_url, c_name):
    return InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text=await inter.get_more(id), url=c_url), InlineKeyboardButton(text=await inter.get_join(id), callback_data=f"register_user_to_course_{c_name}")],
        [InlineKeyboardButton(text=await inter.get_back(id), callback_data="courses_menu")]
    ])


async def get_back(data, id):
    return InlineKeyboardMarkup(inline_keyboard=[[InlineKeyboardButton(text=await inter.get_back(id), callback_data=data)]])

async def answer(user_id):
    return InlineKeyboardMarkup(inline_keyboard=[[InlineKeyboardButton(text="ANSWER", callback_data=f'answer_to_{user_id}')]])