from aiogram import Router, F
from aiogram.types import CallbackQuery
from aiogram.fsm.context import FSMContext

from app.states.states import MainMenu
from app.keyboards import keyboards as kb
from app.services import vacancy_services as v_s
from app.utils.internatinalition import _i18n_ as inter

from translate import Translator

translator = Translator(from_lang='english', to_lang='russian')
v_router = Router()

@v_router.callback_query(F.data == 'vacancies_menu')
async def mentors(callback : CallbackQuery, state : FSMContext):
    await callback.answer(text="Vacancies :")
    await callback.message.answer(text="Vacancies :")
    for v in await v_s.get_vacancies():
        vacancy = f"{v.title}\n\n"
        vacancy += f"{await inter.get_description(callback.from_user.id)} : \n"
        vacancy += translator.translate(v.description)

        await callback.message.answer(text=vacancy, reply_markup=await kb.get_vacancy(callback.from_user.id, v_id=v.id))
    await state.set_state(MainMenu.vacancies_menu)