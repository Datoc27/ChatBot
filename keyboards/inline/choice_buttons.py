from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton


choice = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="Позитив", callback_data="choose:pos"),
            InlineKeyboardButton(text="Негатив", callback_data="choose:neg")
        ],
        [
            InlineKeyboardButton(text="Болдырмау", callback_data="cancel")
        ]
    ]
)

catton = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="Meow", callback_data="cat")
        ]
    ]
)
