from aiogram import Router
from aiogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.filters import CommandStart

router = Router()

@router.message(CommandStart())
async def start_bot(message: Message):
    keyboard = InlineKeyboardMarkup(
        inline_keyboard=[
            [InlineKeyboardButton(text="Найти мероприятие", callback_data="show_info_event")],
            [InlineKeyboardButton(text="Показать ближайшие события", callback_data="show_all_events")],
            [InlineKeyboardButton(text="Получить рекомендации", callback_data="recommend")],
        ]
    )

    await message.answer(
        "Привет! Я помогу найти информацию о фильмах и спектаклях.\n\nВыберите действие:",
        reply_markup=keyboard
    )

def register_handler(dp):
    dp.include_router(router)
