from aiogram.types import Message, CallbackQuery
from aiogram.dispatcher.filters import Command

from keyboards.inline.choice_buttons import choice, catton

from loader import dp, bot
from states.mode import Mode

import random
from glob import glob


@dp.message_handler(commands=['start', 'mode'], state="*")
async def show_modes(message: Message):
    await message.answer(text="2 режімнің біреуін таңдаңыз. \n"
                         "Ботты қолданғыңыз келмесе \"болдырмау\" батырмасына басыңыз",
                         reply_markup=choice)

@dp.message_handler(Command("help"), state="*")
async def commands_help(message: Message):
    await message.answer(text="/start немесе /mode — ботты іске қосады. Дайын болыңыз ;) \n"
                         "/help — ботпен қалай жұмыс істеу керектігін көрсетеді \n"
                            "/misiq немесе /cat — мысық әлеміне қош келдіңіз! \n"
                            "/kick хат — хатты жіберген құрметті мырзаны қуып жібереді\n"
                            "/del хат — таңдаған хатты жояды \n")


@dp.callback_query_handler(text_contains="pos", state="*")
async def choose_pos(call: CallbackQuery):
    await call.answer(cache_time=60)
    await call.message.answer("Позитив режімін таңдадыңыз!")
    await call.message.edit_reply_markup()
    await Mode.pos.set()


@dp.callback_query_handler(text_contains="neg", state="*")
async def choose_pos(call: CallbackQuery):
    await call.answer(cache_time=60)
    await call.message.answer("Негатив режімін таңдадыңыз!")
    await call.message.edit_reply_markup()
    await Mode.neg.set()


@dp.callback_query_handler(text="cancel", state="*")
async def cancel_choice(call: CallbackQuery):
    await call.answer("Болдырмадыңыз", show_alert=True)
    await call.message.edit_reply_markup()


@dp.message_handler(Command("del"), state="*")
async def del_message(message: Message):
    try:
        await bot.delete_message(chat_id=message.chat.id, message_id=message.reply_to_message.message_id)
        await bot.send_message(chat_id=message.chat.id, text="Хат жойылды!")
    except:
        await bot.send_message(chat_id=message.chat.id, text="Ботқа әкімші құқығын беріңіз!")


@dp.message_handler(Command("kick"), state="*")
async def del_message(message: Message):
    try:
        await bot.kick_chat_member(chat_id=message.chat.id, user_id=message.reply_to_message.from_user.id)
        await bot.send_message(chat_id=message.chat.id, text="Адам қуылды!")
    except:
        await bot.send_message(chat_id=message.chat.id, text="Ботқа әкімші құқығын беріңіз!")


@dp.message_handler(commands=['cat', 'misiq'], state="*")
async def cat_button(message: Message):
    await message.answer(text="Мысықты шақыру",
                         reply_markup=catton)


@dp.callback_query_handler(text="cat", state="*")
async def show_cat(call: CallbackQuery):
    await call.answer(cache_time=0)
    cats_gallery = glob("data/cats/*.jpg")
    get_random_cat = random.choice(cats_gallery)
    with open(get_random_cat, 'rb') as photo:
        await bot.send_photo(
            call.message.chat.id,
            photo,
            caption='Мысық мында 😺'
        )
