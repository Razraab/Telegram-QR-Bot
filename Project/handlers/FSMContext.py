from aiogram.dispatcher.filters.state import State, StatesGroup


class FSMContext(StatesGroup):
    dialog = State()
