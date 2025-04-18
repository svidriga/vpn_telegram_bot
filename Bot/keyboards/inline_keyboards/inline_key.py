from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

from Bot.texts.ru_texts import Texts_Russian

inline_keyboard_start_command = InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(text=Texts_Russian.keyboard_start_text, callback_data='get_test_key')],
        [InlineKeyboardButton(text=Texts_Russian.keyboard_menu_text, callback_data='go_menu')]
    ]
)

inline_keyboard_choose_key_from_buy_menu = InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(text=Texts_Russian.add_new_vpn_inline, callback_data='add_new_vpn_with_close')],
        [InlineKeyboardButton(text=Texts_Russian.inline_close, callback_data='close')]
    ]
)

inline_keyboard_buy_message_from_add_new_vpn = InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(text=Texts_Russian.buy_text_inline_1, callback_data='buy_data_1')],
        [InlineKeyboardButton(text=Texts_Russian.buy_text_inline_2, callback_data='buy_data_2')],
        [InlineKeyboardButton(text=Texts_Russian.buy_text_inline_3, callback_data='buy_data_3')],
        [InlineKeyboardButton(text=Texts_Russian.buy_text_inline_4, callback_data='buy_data_4')],
        [InlineKeyboardButton(text=Texts_Russian.buy_text_inline_5, callback_data='buy_data_5')],
        [InlineKeyboardButton(text=Texts_Russian.buy_text_inline_6, callback_data='buy_data_6')],
        [InlineKeyboardButton(text=Texts_Russian.inline_go_back, callback_data='go_back_to_choose_key_from_buy_menu')]
    ]
)

inline_keyboard_buy = InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(text=Texts_Russian.inline_buy, callback_data='buy')],
        [InlineKeyboardButton(text=Texts_Russian.inline_go_back, callback_data='go_back_from_buy')]
    ]
)

inline_keyboard_personal_account_message = InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(text=Texts_Russian.menu_keyboard_key, callback_data='my_keys')],
        [InlineKeyboardButton(text=Texts_Russian.personal_account_inline_bonuses, callback_data='my_bonuses')],
        [InlineKeyboardButton(text=Texts_Russian.keyboard_referral_program, callback_data='referral_program'),
         InlineKeyboardButton(text=Texts_Russian.keyboard_insert_promocode, callback_data='insert_promocode')],
        [InlineKeyboardButton(text=Texts_Russian.inline_close, callback_data='close')]
    ]
)

# inline_keyboard_vpn_settings = InlineKeyboardMarkup(
#     inline_keyboard=[
#         [InlineKeyboardButton(text=Texts_Russian.my_keys_settings_inline, callback_data='vpn1')],
#         [InlineKeyboardButton(text=Texts_Russian.add_new_vpn_inline, callback_data='add_new_vpn')],
#         [InlineKeyboardButton(text=Texts_Russian.inline_go_back, callback_data='go_back_from_vpn_settings')]
#     ]
# )

# inline_keyboard_vpn_settings_go_back_close = InlineKeyboardMarkup(
#     inline_keyboard=[
#         [InlineKeyboardButton(text=Texts_Russian.my_keys_settings_inline, callback_data='vpn1')],
#         [InlineKeyboardButton(text=Texts_Russian.add_new_vpn_inline, callback_data='add_new_vpn')],
#         [InlineKeyboardButton(text=Texts_Russian.inline_go_back, callback_data='go_back_from_vpn_settings_with_close')]
#     ]
# )

# inline_keyboard_vpn_settings_with_close = InlineKeyboardMarkup(
#     inline_keyboard=[
#         [InlineKeyboardButton(text=Texts_Russian.my_keys_settings_inline, callback_data='vpn1_with_close')],
#         [InlineKeyboardButton(text=Texts_Russian.add_new_vpn_inline, callback_data='add_new_vpn_with_close')],
#         [InlineKeyboardButton(text=Texts_Russian.inline_close, callback_data='close')]
#     ]
# )

inline_keyboard_go_back = InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(text=Texts_Russian.inline_go_back, callback_data='go_back_from_bonuses')]
    ]
)

# inline_keyabord_vpn1 = InlineKeyboardMarkup(
#     inline_keyboard=[
#         [InlineKeyboardButton(text=Texts_Russian.my_keys_change_name, callback_data='change_key_name')],
#         [InlineKeyboardButton(text=Texts_Russian.my_keys_change_location, callback_data='change_key_location')],
#         [InlineKeyboardButton(text=Texts_Russian.inline_go_back, callback_data='go_back_from_my_key')]
#     ]
# )


inline_keyboard_buy_message_with_go_back = InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(text=Texts_Russian.buy_text_inline_1, callback_data='buy_data_1')],
        [InlineKeyboardButton(text=Texts_Russian.buy_text_inline_2, callback_data='buy_data_2')],
        [InlineKeyboardButton(text=Texts_Russian.buy_text_inline_3, callback_data='buy_data_3')],
        [InlineKeyboardButton(text=Texts_Russian.buy_text_inline_4, callback_data='buy_data_4')],
        [InlineKeyboardButton(text=Texts_Russian.buy_text_inline_5, callback_data='buy_data_5')],
        [InlineKeyboardButton(text=Texts_Russian.buy_text_inline_6, callback_data='buy_data_6')],
        [InlineKeyboardButton(text=Texts_Russian.inline_go_back, callback_data='go_back_from_buy')]
    ]
)

# inline_keyboard_change_location_key_choose_from_menu = InlineKeyboardMarkup(
#     inline_keyboard=[
#         [InlineKeyboardButton(text=Texts_Russian.my_keys_settings_inline, callback_data='vpn1_temporary_change_location_from_menu')],
#         [InlineKeyboardButton(text=Texts_Russian.inline_close, callback_data='close')]
#     ]
# )

# inline_keyboard_change_location_location_choose_from_menu = InlineKeyboardMarkup(
#     inline_keyboard=[
#         [InlineKeyboardButton(text=Texts_Russian.inline_location_temporary, callback_data='choose_location_temporary')],
#         [InlineKeyboardButton(text=Texts_Russian.inline_go_back, callback_data='go_back_from_choose_country_from_menu')]
#     ]
# )

# inline_keyboard_change_location_location_choose = InlineKeyboardMarkup(
#     inline_keyboard=[
#         [InlineKeyboardButton(text=Texts_Russian.inline_location_temporary, callback_data='choose_location_temporary')],
#         [InlineKeyboardButton(text=Texts_Russian.inline_go_back, callback_data='go_back_from_choose_country')]
#     ]
# )

inline_keyboard_subscribe = InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(text=Texts_Russian.inline_subscribe, callback_data='go_subscribe', url='https://t.me/vpn_jebberg_service')],
        [InlineKeyboardButton(text=Texts_Russian.inline_is_subscribed, callback_data='subscribed_done')]
    ]
)

inline_keyboard_used_trial_info = InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(text=Texts_Russian.inline_get_free_used_yes, callback_data='go_yes_trial')],
        [InlineKeyboardButton(text=Texts_Russian.inline_get_free_used_no, callback_data='go_no_trial')]
    ]
)