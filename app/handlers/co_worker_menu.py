from aiogram import Router, F
from aiogram.types import CallbackQuery, Message
from aiogram.fsm.context import FSMContext

from app.keyboards import keyboards as kb
from app.services import user_service as u_s
from app.data.photo_ids import CO_WORKERS_PHOTO

cw_router = Router()

@cw_router.callback_query(F.data == 'co_worker_menu')
async def co_workers(callback : CallbackQuery, state : FSMContext):
    await callback.answer(text="Co-workers :")
    await callback.message.delete()
    await callback.message.answer_photo(photo=CO_WORKERS_PHOTO, reply_markup=await kb.get_co_workers(callback.from_user.id))

@cw_router.callback_query(F.data.startswith("co_worker_"))
async def co_worker_menu(callback : CallbackQuery, state : FSMContext):
    await callback.answer(text="Co-worker :")
    co_worker = await u_s.get_co_worker(callback.data.split('_')[2])
    await callback.message.delete()
    info = f"{co_worker.firstname} {co_worker.lastname}\n\n\n"
    info += f"\n{co_worker.resume}"
    await callback.message.answer_photo(co_worker.photo_id, caption=info, reply_markup=(await kb.get_co_worker_menu(co_worker, callback.from_user.id)))
    await state.clear()