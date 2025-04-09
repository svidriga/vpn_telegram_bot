import asyncio 

from aiogram.types import CallbackQuery
from aiogram import Router, F

from Bot.texts.ru_texts import Texts_Russian
from Bot.keyboards.keyboards import key
from Bot.keyboards.inline_keyboards import inline_key



router = Router()

@router.callback_query(F.data == 'get_test_key')
async def process_callback_start_command_get(callback: CallbackQuery):
    await callback.message.answer(
        Texts_Russian.give_key_text # далее сделать проверку подписки, а в группе закрепить пост, который рассказывает про все фри движуху
    )

    await callback.answer()

@router.callback_query(F.data == 'go_menu')
async def process_callback_start_command_go(callback: CallbackQuery):
    await callback.message.answer(
        text=Texts_Russian.menu_text,
        reply_markup=key.keyboard_go_menu_callback
    )

    await callback.answer()

@router.callback_query(F.data.in_(['my_keys', 'go_back_from_my_key', 'go_back_from_buy']))
async def process_callback__my_keys(callback : CallbackQuery):
    await callback.message.edit_text(
        text=Texts_Russian.get_all_my_keys,
        reply_markup=inline_key.inline_keyboard_vpn_settings
    )

    await callback.answer()

@router.callback_query(F.data == 'my_bonuses')
async def process_callback_my_bonuses(callback: CallbackQuery):
    await callback.message.edit_text(
        text=Texts_Russian.personal_account_inline_bonuses,
        reply_markup=inline_key.inline_keyboard_go_back
    )

    await callback.answer()

@router.callback_query(F.data == 'close')
async def process_callback_close(callback: CallbackQuery):
    await callback.message.delete()

@router.callback_query(F.data.in_(['go_back_from_bonuses', 'go_back_from_vpn_settings']))
async def process_callback_go_back_from_bonueses(callback: CallbackQuery):
    await callback.message.edit_text(
        text=Texts_Russian.personal_account_text,
        reply_markup=inline_key.inline_keyboard_personal_account_message
    )

    await callback.answer()

@router.callback_query(F.data.in_(['vpn1', 'go_back_from_choose_country']))
async def process_callback_vpn1(callback: CallbackQuery):
    await callback.message.edit_text(
        text=Texts_Russian.my_keys_settings_temporary,
        reply_markup=inline_key.inline_keyabord_vpn1
    )

    await callback.answer()

@router.callback_query(F.data == 'add_new_vpn')
async def process_callback_vpn1(callback: CallbackQuery):
    await callback.message.edit_text(
        text=Texts_Russian.buy_text,
        reply_markup=inline_key.inline_keyboard_buy_message_with_go_back
    )

    await callback.answer()

@router.callback_query(F.data == 'choose_location_temporary')
async def process_callback_choose_location_temporary(callback: CallbackQuery):
    await callback.message.edit_text(
        text=Texts_Russian.message_change_location_complete
    )

    await callback.answer()

@router.callback_query(F.data == 'vpn1_temporary_change_location_from_menu')
async def process_callback_vpn1_temporary_change_location_from_menu(callback: CallbackQuery):
    await callback.message.edit_text(
        text=Texts_Russian.message_change_location_country_choose,
        reply_markup=inline_key.inline_keyboard_change_location_location_choose_from_menu
    )

    await callback.answer()

@router.callback_query(F.data == 'go_back_from_choose_country_from_menu')
async def process_callback_go_back_from_choose_country_from_menu(callback: CallbackQuery):
    await callback.message.edit_text(
        text=Texts_Russian.message_change_location_key_choose,
        reply_markup=inline_key.inline_keyboard_change_location_key_choose_from_menu
    )

    await callback.answer()

@router.callback_query(F.data == 'change_key_location')
async def process_callback_change_key_location(callback: CallbackQuery):
    await callback.message.edit_text(
        text=Texts_Russian.message_change_location_country_choose,
        reply_markup=inline_key.inline_keyboard_change_location_location_choose
    )

    await callback.answer()