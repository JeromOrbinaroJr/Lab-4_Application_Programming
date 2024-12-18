from aiogram import Router
from aiogram.filters import Command
from aiogram.fsm.context import FSMContext
from aiogram.types import Message
from parsers.cinema_parser import get_film_by_name, get_three_films
from parsers.performance_parser import get_performance_by_title, get_three_performances
from aiogram.fsm.state import State, StatesGroup

router = Router()

class EventState(StatesGroup):
    waiting_for_event_name = State()

@router.message(EventState.waiting_for_event_name)
async def handle_event_name(message: Message, state: FSMContext):
    title_event = message.text.strip()

    if not title_event:
        await message.answer("⚠ Пожалуйста, введите корректное название мероприятия.")
        return

    # Check if film is found
    films = get_film_by_name(title_event)
    if films:
        response_text = "🎬 Найденные фильмы:\n\n"
        for film in films:
            response_text += f"📌 *Название*: {film['title']}\n📖 *Описание*: {film['description']}\n📅 *Год*: {film['year']}\n\n"
        await message.answer(response_text, parse_mode="Markdown")
    else:
        # Check if performance is found
        performances = get_performance_by_title(title_event)
        if performances:
            response_text = "🎭 Найденные спектакли:\n\n"
            for performance in performances:
                response_text += f"📌 *Название*: {performance['title']}\n📖 *Место*: {performance['place']}\n📅 *Дата*: {performance['dates']}\n\n"
            await message.answer(response_text, parse_mode="Markdown")
        else:
            await message.answer(f"❌ Мероприятие с названием '{title_event}' не найдено.")
    await state.clear()

@router.message(Command("show_all_events"))
async def few_events(message: Message):
    films = get_three_films()
    performances = get_three_performances()

    response_text = "🎬 *Фильмы*\n\n"
    response_text += "\n".join(
        [f"📌 *Название*: {film['title']}\n📖 *Жанр*: {film['description']}\n📅 *Год*: {film['year']}" for film in films]
    ) or "❌ Фильмы не найдены."

    response_text += "\n\n🎭 *Спектакли*\n\n"
    response_text += "\n".join(
        [f"📌 *Название*: {performance['title']}\n📖 *Место*: {performance['place']}\n📅 *Дата*: {performance['dates']}" for performance in performances]
    ) or "❌ Спектакли не найдены."

    await message.answer(response_text, parse_mode="Markdown")

def register_handler(dp):
    dp.include_router(router)
