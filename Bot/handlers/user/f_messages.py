from aiogram import Router, F
from aiogram.types import Message
from aiogram.fsm.context import FSMContext

from Bot.texts.ru_texts import Texts_Russian
from Bot.keyboards.inline_keyboards import inline_key
from Bot.database.get_referral_code import get_referral_code

router = Router()

@router.message(F.text == Texts_Russian.keyboard_start_text)
async def get_trial(message: Message, state: FSMContext):
    data = await state.get_data()
    data_used_trial_subscription = data.get('used_trial_subscription')

    if data_used_trial_subscription is False:
        await message.answer(
            text=Texts_Russian.give_key_text,
            reply_markup=inline_key.inline_keyboard_subscribe
        )
    else:
        await message.answer(
            text=Texts_Russian.message_get_free_used,
            reply_markup=inline_key.inline_keyboard_used_trial_info
        )

@router.message(F.text == Texts_Russian.menu_keyboard_key)
async def get_key(message: Message):
    await message.answer(
        text=Texts_Russian.get_all_my_keys,
        reply_markup=inline_key.inline_keyboard_vpn_settings_with_close
    )

@router.message(F.text == Texts_Russian.menu_keyboard_personal_account)
async def personal_account(message: Message):
    await message.answer(
        text=Texts_Russian.personal_account_text, 
        reply_markup=inline_key.inline_keyboard_personal_account_message
    )

@router.message(F.text == Texts_Russian.menu_keyboard_buy)
async def buy_subscription(message: Message):
    await message.answer(
        text=Texts_Russian.message_buy_choose_key, 
        reply_markup=inline_key.inline_keyboard_choose_key_from_buy_menu
    )

@router.message(F.text == Texts_Russian.menu_keyboard_change_location)
async def change_location(message: Message):
    await message.answer(
        text=Texts_Russian.message_change_location_key_choose,
        reply_markup=inline_key.inline_keyboard_change_location_key_choose_from_menu
    )

@router.message(F.text == Texts_Russian.menu_keyboard_info)
async def get_info(message: Message):
    await message.answer(
        text=Texts_Russian.get_info_text
    )

@router.message(F.text == Texts_Russian.menu_keyboard_support)
async def get_support(message: Message):
    await message.answer(
        text=f'<b>{Texts_Russian.support_text_part_one}</b>{Texts_Russian.support_text_part_two}'
    )

@router.message(F.text == Texts_Russian.menu_keyboard_about)
async def get_about(message: Message):
    await message.answer(
        text=Texts_Russian.about_text
    )

@router.message(F.text == Texts_Russian.keyboard_referral_program)
async def referral_program(message: Message):
    user_id = message.from_user.id
    referral_code = await get_referral_code(user_id)
    referral_link = f't.me/vpn_jebberg_service_bot?start={referral_code}'
    await message.answer(
        text=f'{Texts_Russian.message_referral_program_part_one} <b>{referral_link}</b>{Texts_Russian.message_referral_program_part_two}'
    )

@router.message(F.text == Texts_Russian.keyboard_insert_promocode)
async def insert_promocode(message: Message):
    await message.answer(
        text=Texts_Russian.message_insert_promocode
    )