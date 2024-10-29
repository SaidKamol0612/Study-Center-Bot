from aiogram.fsm.context import FSMContext

from app.database import requests as rq
from app.database.models import User
from app.utils.internatinalition import _i18n_ as inter

async def set_user(user_id):
    await rq.set_user(user_id)

async def get_co_worker(id):
    return await rq.get_co_worker(id)

async def add_user(state : FSMContext):
    data = await state.get_data()
    new_user = User(firstname=data['enter_name'], phone=data['enter_num'], reason=data['reason'], is_seen='no')

    await rq.add_user(new_user)

async def get_f_info(id, state : FSMContext):
    data = await state.get_data()

    res = ""
    if (await inter.get_lang(id)) == 'uz':
        res += f"Ism : {data['enter_name']}"
        res += f"\nTelefon raqami : {data['enter_num']}"
    else:
        res += f"Имя : {data['enter_name']}"
        res += f"\nНомер телефона : {data['enter_num']}"
    return res
    