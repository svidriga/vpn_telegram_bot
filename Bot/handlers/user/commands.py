from aiogram import Router
from aiogram.filters import Command
from aiogram.types import Message

from Bot.texts.ru_texts import Texts_Russian
from Bot.keyboards.inline_keyboards import inline_key

router = Router()

@router.message(Command('start'))
async def start_command(message: Message):
    await message.answer(
        f'<b>{Texts_Russian.hello_text_part_one} <i>{message.from_user.first_name or 'друг'}!</i>{Texts_Russian.hello_text_part_two}</b>'
    )

    await message.answer(
        Texts_Russian.start_text,
        reply_markup=inline_key.inline_keyboard_start_command
    )