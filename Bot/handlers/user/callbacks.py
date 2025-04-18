from aiogram.types import CallbackQuery
from aiogram import Router, F
from aiogram.fsm.state import State, StatesGroup
from aiogram.fsm.context import FSMContext

from Bot.texts.ru_texts import Texts_Russian
from Bot.keyboards.keyboards import key
from Bot.keyboards.inline_keyboards import inline_key
from Bot.fsm_machine.fsm_classes import TrialStatus
from Bot.database.give_key_to_user import give_key_to_user


router = Router()

@router.callback_query(F.data == 'get_test_key')
async def process_callback_start_command_get(callback: CallbackQuery):
    await callback.message.answer(
        text=Texts_Russian.give_key_text,
        reply_markup=inline_key.inline_keyboard_subscribe
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

@router.callback_query(F.data == 'go_back_from_bonuses')
async def process_callback_go_back_from_bonueses(callback: CallbackQuery):
    await callback.message.edit_text(
        text=Texts_Russian.personal_account_text,
        reply_markup=inline_key.inline_keyboard_personal_account_message
    )

    await callback.answer()

# @router.callback_query(F.data.in_(['vpn1', 'go_back_from_choose_country']))
# async def process_callback_vpn1(callback: CallbackQuery):
#     await callback.message.edit_text(
#         text=Texts_Russian.my_keys_settings_temporary,
#         reply_markup=inline_key.inline_keyabord_vpn1
#     )

#     await callback.answer()


# @router.callback_query(F.data == 'add_new_vpn')
# async def process_callback_vpn1(callback: CallbackQuery):
#     await callback.message.edit_text(
#         text=Texts_Russian.buy_text,
#         reply_markup=inline_key.inline_keyboard_buy_message_with_go_back
#     )

#     await callback.answer()

# @router.callback_query(F.data == 'choose_location_temporary')
# async def process_callback_choose_location_temporary(callback: CallbackQuery):
#     await callback.message.edit_text(
#         text=Texts_Russian.message_change_location_complete
#     )

#     await callback.answer()

# @router.callback_query(F.data == 'vpn1_temporary_change_location_from_menu')
# async def process_callback_vpn1_temporary_change_location_from_menu(callback: CallbackQuery):
#     await callback.message.edit_text(
#         text=Texts_Russian.message_change_location_country_choose,
#         reply_markup=inline_key.inline_keyboard_change_location_location_choose_from_menu
#     )

#     await callback.answer()

# @router.callback_query(F.data == 'go_back_from_choose_country_from_menu')
# async def process_callback_go_back_from_choose_country_from_menu(callback: CallbackQuery):
#     await callback.message.edit_text(
#         text=Texts_Russian.message_change_location_key_choose,
#         reply_markup=inline_key.inline_keyboard_change_location_key_choose_from_menu
#     )

#     await callback.answer()

# @router.callback_query(F.data == 'change_key_location')
# async def process_callback_change_key_location(callback: CallbackQuery):
#     await callback.message.edit_text(
#         text=Texts_Russian.message_change_location_country_choose,
#         reply_markup=inline_key.inline_keyboard_change_location_location_choose
#     )

#     await callback.answer()

@router.callback_query(F.data == 'subscribed_done')
async def process_callback_subscribed_done(callback: CallbackQuery, state: FSMContext):
    try:
        from Bot.main.bot import bot
        member = await bot.get_chat_member(
            chat_id='@vpn_jebberg_service',
            user_id=callback.from_user.id
        )

        if member.status == 'member' or member.status == 'creator':

            await callback.message.answer(
                text=Texts_Russian.menu_text,
                reply_markup=key.keyboard_go_menu_callback
            )

            await callback.message.answer(
                text=Texts_Russian.here_is_your_key_deleter_after
            )
            await callback.answer()
            await callback.message.delete()
            await state.update_data(used_trial_subscription=True)
            await state.set_state(None)
        else:
            await callback.answer(
                text=Texts_Russian.here_is_your_key_deleter_after
            )

    except Exception as e:
        await callback.answer(
            text=Texts_Russian.message_getting_subscribed_status_error
        )
        print(f'error is {e}')
    data = await state.get_data()
    for_print = data.get('used_trial_subscription')
    print(f'подписка {for_print}')

@router.callback_query(F.data == 'go_yes_trial')
async def process_callback_go_yes(callback: CallbackQuery):
    await callback.message.edit_text(
        text=Texts_Russian.message_tell_about_free
    )
    await callback.answer()

@router.callback_query(F.data == 'go_no_trial')
async def process_callback_go_no(callback: CallbackQuery):
    await callback.message.edit_text(
        text=Texts_Russian.message_dont_tell_about_free
    )
    await callback.answer()

@router.callback_query(F.data == 'add_new_vpn_with_close')
async def process_callback_add_new_vpn_with_close(callback: CallbackQuery):
    await callback.message.edit_text(
        text=Texts_Russian.message_tariff_choose,
        reply_markup=inline_key.inline_keyboard_buy_message_from_add_new_vpn
    )
    await callback.answer()

@router.callback_query(F.data == 'go_back_to_choose_key_from_buy_menu')
async def process_callback_go_back_to_choose_key_from_buy_menu(callback: CallbackQuery):
    await callback.message.edit_text(
        text=Texts_Russian.message_buy_choose_key,
        reply_markup=inline_key.inline_keyboard_choose_key_from_buy_menu
    )
    await callback.answer()


@router.callback_query(F.data.in_(['go_back_from_buy', 'buy_data_1']))
async def process_callback_buy_data(callback: CallbackQuery):
    await callback.message.edit_text(
        text=Texts_Russian.message_buy_data_menu,
        reply_markup=inline_key.inline_keyboard_buy
    )
    await callback.answer()

@router.callback_query(F.data == 'buy')
async def process_callback_buy(callback: CallbackQuery):
    user_id = callback.from_user.id
    duration = 1
    key, location = await give_key_to_user(user_id, duration)


    await callback.message.edit_text(
        text=f'{Texts_Russian.message_buy_is_done} {key} {location}'
    )
    await callback.answer()   