from loader import dp
from states.mode import Mode
from aiogram.types import Message


@dp.message_handler(state=Mode.pos)
async def long_mes(message: Message):
    max_l = 256
    if len(message.text) > max_l:
        await message.answer(text="Лонгридтерді сүйемін. Тағы бола ма?)")

@dp.message_handler(content_types=['photo'], state=Mode.pos)
async def photo(message):
    await message.answer(text="Әдемі сурет — менен құрмет👍")


@dp.message_handler(content_types=['video'], state=Mode.pos)
async def photo(message):
    await message.answer(text="Ал, попкорн алып көрейік🍿")



@dp.message_handler(content_types=['voice'], state=Mode.pos)
async def photo(message):
    await message.answer(text="🎵тәтті тәтті дауыс")
