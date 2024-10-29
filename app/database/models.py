from sqlalchemy import BigInteger
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy.ext.asyncio import AsyncAttrs, async_sessionmaker, create_async_engine

from app.data.config import DATABASE_URL

engine = create_async_engine(url=DATABASE_URL)

async_session = async_sessionmaker(engine)

class Base(DeclarativeBase, AsyncAttrs):
    pass

class CoWorker(Base):
    __tablename__ = 'co_workers'

    id: Mapped[int] = mapped_column(primary_key=True)
    firstname : Mapped[str] = mapped_column()
    lastname : Mapped[str] = mapped_column()
    photo_id : Mapped[str] = mapped_column()
    resume : Mapped[str] = mapped_column()
    link_contact : Mapped[str] = mapped_column()

class UserLang(Base):
    __tablename__ = 'user_langs'

    id: Mapped[int] = mapped_column(primary_key=True)
    tg_id = mapped_column(BigInteger)
    sys_lang: Mapped[str] = mapped_column()

class User(Base):
    __tablename__ = 'users'

    id: Mapped[int] = mapped_column(primary_key=True)
    firstname : Mapped[str] = mapped_column()
    phone: Mapped[str] = mapped_column()
    reason: Mapped[str] = mapped_column()
    is_seen: Mapped[str] = mapped_column()

class Vacancy(Base):
    __tablename__ = 'vacancies'

    id: Mapped[int] = mapped_column(primary_key=True)
    title: Mapped[str] = mapped_column()
    description: Mapped[str] = mapped_column()

class Lang():
    def __init__(self, lang) -> None:
        self.language = lang

async def async_main():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)