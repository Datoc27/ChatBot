from aiogram.dispatcher.filters.state import StatesGroup, State


class Mode(StatesGroup):
    pos = State()
    neg = State()
