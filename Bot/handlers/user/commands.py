from aiogram import Router
from aiogram.filters import Command
from aiogram.types import Message

from Bot.texts.ru_texts import Texts_Russian
from Bot.keyboards.inline_keyboards import inline_key
from Bot.database.add_user_to_db import add_user_to_db, add_user_to_db_no_ref

router = Router()

@router.message(Command('start'))
async def start_command(message: Message):
    user_id = message.from_user.id
    username = message.from_user.username
    try:
        referred_by = message.text.split()[1]
        await add_user_to_db(user_id, username, referred_by)
    except:
        await add_user_to_db_no_ref(user_id, username)

    await message.answer(
        f'<b>{Texts_Russian.hello_text_part_one} <i>{message.from_user.first_name or 'друг'}!</i>{Texts_Russian.hello_text_part_two}</b>'
    )

    await message.answer(
        Texts_Russian.start_text,
        reply_markup=inline_key.inline_keyboard_start_command
    )