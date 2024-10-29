from app.database import requests as rq

async def set_lang(lang, user_id):
    await rq.set_lang(lang, user_id)

async def get_lang(id):
    return await rq.get_lang(id)

async def get_info(id):
    app_lang = await rq.get_lang(id)
    if app_lang == 'uz':
        return "Tramplin IT Akademiyasida siz Dasturlashni Professionallardan o'rganishingiz mumkin\n\nKurs davomida yuqori malakali dasturchilardan maxsus metodika asosida sifatli ta’lim olishingiz va o’zlashtirgan bilimlaringizni amaliyotda 50 dan ortiq loyiha asosida o’z portfolioingizni yaratishingiz mumkin\n\nIsh bilan ta’minlaymiz agar\n\n- Interview\n- Vazifalar\n- Imtihon\n- Kitob taqdimoti\n- Mini guruhlar\n\nYuqoridagilardan 90+/100 olsangiz"
    elif app_lang == 'ru':
        return "В IT Академии Трамплин вы можете научиться программированию у профессионалов.\n\nВ ходе курса вы сможете получить качественное образование от высококвалифицированных программистов по специальной методике, а также сможете применить полученные знания на практике и создать собственное портфолио на основе более 50 проектов\n\nОбучение с работой поехали, если\n\n- Интервью\n- Задания\n- Экзамен\n- Презентация книги\n- Мини-группы\n\nЕсли вы набрали 90+/100 из вышеперечисленного"

async def get_main_menu(id):
    app_lang = await rq.get_lang(id)
    if app_lang == 'uz':
        return ["🧑‍💻Xodimlar", "📚Kurslar", "Biz haqimida", "🕵️Vakansiyalar", "🔗Biz bilan bog'lanish", '⚙️Sozlamalar']
    else:
        return ["🧑‍💻Сотрудники", "📚Курсы", "О нас", "🕵️Вакансии", "🔗Связаться с нами", '⚙️Настройки']
    
async def get_courses(id):
    app_lang = await rq.get_lang(id)
    if app_lang == 'uz':
        return ["🌐Frontend", "🧠Backend", "🛡Kiber Xavsizlik", "🎨Grafik Dizayn", "🔙Ortga"]
    else:
        return ["🌐Фронтенд", "🧠Бэкенд", "🛡Кибер Безопасность", "🎨График Дизайн", "🔙Назад"]
    
async def get_back(id):
    app_lang = await rq.get_lang(id)
    if app_lang == 'uz':
        return "🔙Ortga"
    else:
        return "🔙Назад"
    
async def get_contact_us(id):
    app_lang = await rq.get_lang(id)
    if app_lang == 'uz':
        return "🔗Bog'lanish"
    else:
        return "🔗Связаться"
    
async def get_join(id):
    app_lang = await rq.get_lang(id)
    if app_lang == 'uz':
        return "➕Yozilish"
    else:
        return "➕Присоединиться"
    
async def get_courses_info(id):
    app_lang = await rq.get_lang(id)
    if app_lang == 'uz':
        return [
            "Tramplin IT Akademiyasida Backend-Python kursi sizga turli texnologiyalar va ramkalar yordamida veb-ilovalar va telegram botlarining backendini qanday yaratishni o'rgatadigan kursdir. Siz Python tilining asoslari, uning sintaksisi, ma'lumotlar tuzilmalari, funksiyalari, sinflari va modullarini o'rganasiz. Shuningdek, siz ma'lumotlar bazalari, xususan PostgreSQL bilan ishlash asoslari bilan tanishasiz va jadvallardan ma'lumotlarni qanday yaratish, o'zgartirish o'rganasiz. ",
            "Front- End dasturlash - bu dasturlash kasbini eng asosiy tushunchalardan tortib to‘liq ish vositalariga ega bo‘lgan ishonchli mutaxassis darajasigacha o‘zlashtirish uchun mo‘ljallangan kurs hisoblanadi. \nUshbu kurs HTML, CSS va JavaScript asoslarini, shuningdek,web dasturlashning eng yaxshi amaliyotlari va adaptiv dizayn texnikasini qamrab oladi.",
            "Kiberxavfsizlik – bu axborot texnologiyalari tizimlari va tarmoklarini xujumlardan ximoya kiladi. Xozirgi kunda xakerlar turli yullar bilan rakamli tizim orkali bankdagi pullarni o'marishadi, yeki plastik kartangizdan pullarni yechib ketishi mumkin. Kiberxavfsizlik aynan ana shunday jinoiy ilarning oldini oladi.",
            "Kundalik hayotimizda uchratadigan barcha reklama mahsulotlari, logotiplar, ijtimoiy tarmoq postlari, mahsulot qadoqlari, jurnal va katalog dizaynlari grafik dizaynerlar tomonidan tayyorlanadi:\n\nKurs davomiyligi 6 oy, haftada 3 marta 1.5 soatdan iborat\n\nDarslarimizni 8+ yil tajribaga ega mentorlar tomonidan olib boriladi"
        ]
    else:
        return [
            "Курс Backend-Python в Tramplin IT Academy — это курс, который научит создавать серверную часть веб-приложений и ботов Telegram с использованием различных технологий и фреймворков. Вы изучите основы языка Python, его синтаксис, структуры данных, функции. , классы и модули. Также вы познакомитесь с основами работы с базами данных, в частности с PostgreSQL, и научитесь создавать и изменять данные из таблиц.",
            "Внешнее программирование — это курс, предназначенный для того, чтобы вывести профессию программиста от самых базовых концепций к уверенному профессиональному уровню с полным набором рабочих инструментов. \nЭтот курс охватывает основы HTML, CSS и JavaScript, а также самые основные аспекты веб-программирование охватывает лучшие практики и методы адаптивного дизайна",
            "Кибербезопасность защищает системы и сети информационных технологий от атак. Сегодня хакеры крадут деньги из банка с помощью цифровой системы различными способами или могут снять деньги с вашей пластиковой карты. Кибербезопасность предотвращает подобные преступления.",
            "Вся рекламная продукция, логотипы, посты в социальных сетях, упаковка продукции, дизайн журналов и каталогов, с которыми мы сталкиваемся в повседневной жизни, созданы графическими дизайнерами:\n\nПродолжительность курса 6 месяцев по 1,5 часа 3 раза в неделю\n\nНаш курс занятия ведут наставники с опытом работы более 8 лет."
        ]

async def get_admin(id):
    app_lang = await rq.get_lang(id)
    if app_lang == 'uz':
        return "Sizning so'rovingiz yuborildi. Bizning administratorlarimiz tez orada siz bilan bog'lanadi."
    else:
        return "Ваш запрос отправлен. Наши администраторы свяжутся с вами в ближайшее время."
    
async def get_ent_num(id):
    app_lang = await rq.get_lang(id)
    if app_lang == 'uz':
        return "📞Telefon raqamingizni kiriting : "
    else:
        return "📞Введите номер телефона : "
    
async def get_ent_name(id):
    app_lang = await rq.get_lang(id)
    if app_lang == 'uz':
        return "Ismingizni kiriting : "
    else:
        return "Введите своё имя : "

async def get_settings(id):
    app_lang = await rq.get_lang(id)
    if app_lang == 'uz':
        return ['Tilni tanlash', '💬Komentariya qoldirish']
    else:
        return ['Выбрать язык', '💬Оставить отзыв']
    
async def get_comment(id):
    app_lang = await rq.get_lang(id)
    if app_lang == 'uz':
        return "Kommentariyangizni yozing : "
    else:
        return "Напишите ваш комментарий : "
    
async def get_s_comm(id):
    app_lang = await rq.get_lang(id)
    if app_lang == 'uz':
        return "Kommentariyangiz muavafiqiyatli qabul qilindi !"
    else:
        return "Ваш комментарий успешно принят !"
    
async def get_more(id):
    app_lang = await rq.get_lang(id)
    if app_lang == 'uz':
        return "ℹ️Ko'proq ma'lumot"
    else:
        return "ℹ️Узнать больше"
async def get_description(id):
    app_lang = await rq.get_lang(id)
    if app_lang == 'uz':
        return "Tavsif"
    else:
        return "Описание"