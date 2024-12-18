from aiogram import Router
from aiogram.filters import Command
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import StatesGroup, State
from aiogram.types import Message, ReplyKeyboardMarkup, KeyboardButton
from parsers.cinema_parser import get_films_by_genre

router = Router()

class RecommendState(StatesGroup):
    choosing_genre = State()

@router.message(Command("recommend"))
async def recommend_start(message: Message, state: FSMContext):
    keyboard = ReplyKeyboardMarkup(
        keyboard=[
            [KeyboardButton(text="Комедия"), KeyboardButton(text="Драма")],
            [KeyboardButton(text="Боевик"), KeyboardButton(text="Мелодрама")]
        ],
        resize_keyboard=True
    )
    await message.answer("👋 Пожалуйста, выберите жанр фильма:", reply_markup=keyboard)
    await state.set_state(RecommendState.choosing_genre)

@router.message(RecommendState.choosing_genre)
async def recommend_choose_genre(message: Message, state: FSMContext):
    genre = message.text.strip().lower()

    allowed_genres = ["комедия", "драма", "боевик", "мелодрама"]

    if genre not in allowed_genres:
        await message.answer("⚠ Пожалуйста, выберите жанр из предложенных вариантов.")
        return

    recommendations = get_films_by_genre(genre)

    if not recommendations:
        await message.answer("😔 К сожалению, мы не нашли фильмов по вашему запросу.")
        await state.clear()
        return

    response_text = "🎯 Рекомендации фильмов по вашему запросу:\n\n"
    for rec in recommendations:
        response_text += f"🎬 *Название*: {rec['title']}\n📖 *Описание*: {rec['description']}\n📅 *Год*: {rec['year']}\n\n"

    await message.answer(response_text, parse_mode="Markdown")
    await state.clear()

def register_handler(dp):
    dp.include_router(router)
