from aiogram import Router
from aiogram.filters import Command
from aiogram.types import Message
from parsers.cinema_parser import get_film_by_name

router = Router()

@router.message(Command("show_info_event"))
async def event_info(message: Message):
    title_film = message.text[len("/show_info_event "):].strip()

    if not title_film:
        await message.answer(
            "⚠ Пожалуйста, укажите название фильма после команды.\nПример: `/show_info_event Интерстеллар`")
        return

    films = get_film_by_name(title_film)

    if not films:
        await message.answer(f"❌ Фильм с названием '{title_film}' не найден.")
    else:
        response_text = "🎬 Найденные фильмы:\n\n"
        for film in films:
            response_text += (
                f"📌 *Название*: {film['title']}\n"
                f"📖 *Описание*: {film['description']}\n"
                f"📅 *Год*: {film['year']}\n\n"
            )
        await message.answer(response_text, parse_mode="Markdown")

def register_handler(dp):
    dp.include_router(router)