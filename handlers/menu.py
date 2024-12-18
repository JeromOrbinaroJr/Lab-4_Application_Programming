from aiogram.fsm.context import FSMContext
from aiogram.types import CallbackQuery
from aiogram import Router
from handlers.messages import EventState

router = Router()

@router.callback_query(lambda c: c.data in ["show_all_events", "recommend"])
async def handle_menu(callback: CallbackQuery, state: FSMContext):
    if callback.data == "show_all_events":
        from handlers.messages import few_events
        await few_events(callback.message)
    elif callback.data == "recommend":
        from handlers.recommend import recommend_start
        await recommend_start(callback.message, state)

    await callback.answer()

@router.callback_query(lambda c: c.data == "show_info_event")
async def handle_show_info_event(callback: CallbackQuery, state: FSMContext):
    await callback.message.answer("Введите название мероприятия:")
    await state.set_state(EventState.waiting_for_event_name)
    await callback.answer()

def register_handler(dp):
    dp.include_router(router)
