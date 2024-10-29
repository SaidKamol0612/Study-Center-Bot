from app.database import requests as rq

async def get_vacancies():
    return await rq.get_vacancies()