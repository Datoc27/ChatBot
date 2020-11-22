from loader import dp
from states.mode import Mode
from aiogram.types import Message


@dp.message_handler(state=Mode.neg)
async def long_mes(message: Message):
    max_l = 256
    if len(message.text) > max_l:
        await message.answer(text="Мм, өте қызық екен. Ойды қысқа жеткізіп үйрену керек)")


@dp.message_handler(content_types=['photo'], state=Mode.neg)
async def photo(message):
    await message.answer(text="Сұрамаған жерден сурет жібере бермеші!")


@dp.message_handler(content_types=['video'], state=Mode.neg)
async def photo(message):
    await message.answer(text="Біреу қарайды деп ойлайсың ба?)")


@dp.message_handler(content_types=['voice'], state=Mode.neg)
async def photo(message):
    await message.answer(text="Дауысхатыңды жылдам жойып жібер! Біреу даусыңды естіп, есінен танып қалмасын")
