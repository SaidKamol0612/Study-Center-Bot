from app.database.models import async_session
from app.database.models import CoWorker, User, Vacancy, UserLang
from sqlalchemy import select

async def set_user(user_id):
    async with async_session() as session:
        old_user = await session.scalar(select(UserLang).where(UserLang.tg_id == user_id))
        
        if not old_user:
            session.add(UserLang(tg_id=user_id, sys_lang='uz'))

            await session.commit()

async def set_lang(lang, user_id):
    async with async_session() as session:
        u = await session.scalar(select(UserLang).where(UserLang.tg_id == user_id))

        u.sys_lang = lang

        await session.commit()
    
async def get_lang(tg_id):
    async with async_session() as session:
        u = await session.scalar(select(UserLang).where(UserLang.tg_id == tg_id))

        return u.sys_lang

async def get_co_workers():
    async with async_session() as session:
        return await session.scalars(select(CoWorker))

async def get_co_worker(id):
    async with async_session() as session:
        return await session.scalar(select(CoWorker).where(CoWorker.id == id))
    
async def add_user(new_user : User):
    async with async_session() as session:
        user = await session.scalar(select(User).where(User.phone == new_user.phone))

        if not user:
            session.add(new_user)

            await session.commit()

async def get_vacancies():
    async with async_session() as session:
        return await session.scalars(select(Vacancy))