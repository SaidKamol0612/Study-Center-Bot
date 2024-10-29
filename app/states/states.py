from aiogram.fsm.state import StatesGroup, State

class MainMenu(StatesGroup):
    main_menu = State()
    co_workers_menu = State()
    courses_menu = State()
    about_menu = State()
    vacancies_menu = State()
    contact_us_menu = State()
    settings_menu = State()

class Reg(StatesGroup):
    reason = State()
    enter_num = State()
    enter_name = State()

class Comment(StatesGroup):
    description = State()

class AdminAnswer(StatesGroup):
    to_id = State()
    description = State()