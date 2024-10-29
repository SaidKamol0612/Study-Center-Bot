from aiogram import Router, F
from aiogram.types import CallbackQuery, Message
from aiogram.fsm.context import FSMContext

from app.services import user_service as u_s
from app.states.states import Reg
from app.utils.internatinalition import _i18n_ as inter

from app.states.states import MainMenu

from app.utils.notify_admins import notify_admin
from app.data.photo_ids import TRAMPLIN_PHOTO_ID
from app.keyboards import keyboards as kb

c_u_router = Router()

@c_u_router.callback_query(F.data == 'contact_us_menu')
async def mentors(callback : CallbackQuery, state : FSMContext):
    await callback.answer(text="Registration :")
    await callback.message.delete()
    await state.set_state(Reg.reason)
    await state.update_data(reason="to_contact")
    await state.set_state(Reg.enter_num)
    await callback.message.answer(text=(await inter.get_ent_num(callback.from_user.id)))

@c_u_router.callback_query(F.data.startswith('register_user_'))
async def join_to_course(callback : CallbackQuery, state : FSMContext):
    await callback.answer(text="Registration :")
    await state.set_state(Reg.reason)
    data = callback.data.split('_')
    reason = ""
    for i in range(2, len(data)):
        reason += data[i] + "_"

    await state.update_data(reason=reason)
    await state.set_state(Reg.enter_num)
    await callback.message.answer(text=await inter.get_ent_num(callback.from_user.id))

@c_u_router.message(Reg.enter_num)
async def reg_ent_num(message : Message, state : FSMContext):
    await state.update_data(enter_num=message.text)
    await state.set_state(Reg.enter_name)
    await message.reply(text=(await inter.get_ent_name(message.from_user.id)))

@c_u_router.message(Reg.enter_name)
async def reg_ent_num(message : Message, state : FSMContext):
    await state.update_data(enter_name=message.text)
    await u_s.add_user(state)
    info = await u_s.get_f_info(message.from_user.id, state)
    admin_info = ''
    reas_data = (await state.get_data())
    reas = reas_data['reason']
    if reas.startswith('to_course_'):
        c = reas.split('_')[2]
        admin_info += f'\n{c} - kursga yozilmoqchi.'
    elif reas.startswith('to_contact'):
        admin_info += f'\nMa\'lumot olmoqchi.'
    elif reas.startswith('to_vacancy_') :
        v_id = reas.split('_')[2]
        admin_info += f'\nID : {v_id} - Vakansiya haqida ma\'lumot olmoqchi.'

    await notify_admin(info=info+admin_info, user_id=message.from_user.id)

    info += f"\n{await inter.get_admin(message.from_user.id)}"
    await state.set_state(MainMenu.main_menu)
    await message.reply(text=info)    
    await message.answer_photo(photo=TRAMPLIN_PHOTO_ID,caption="Menu :", reply_markup=await kb.get_main_menu(message.from_user.id))
    await state.clear()