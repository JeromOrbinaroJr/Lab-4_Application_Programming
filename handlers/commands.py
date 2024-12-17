from aiogram import Router
from aiogram.types import Message
from aiogram.filters import Command, CommandStart

router = Router()

@router.message(CommandStart())
async def start_bot(message: Message):
    await message.answer("Привет! Я помогу найти информацию о фильмах и спектаклях.\n\n"
        "Доступные команды:\n"
        "/show_info_event [название мероприятия] - Найти информацию о фильме/спектакле.\n"
        "/show_all_events - Показать 3 фильма и 3 спектакля.\n"
        "/recommend - Настроить предпочтения и получить рекомендации.\n"
        )

def register_handler(dp):
    dp.include_router(router)