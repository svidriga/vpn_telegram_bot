from aiogram import Router, F
from aiogram.filters import Command
from aiogram.types import Message
from aiogram.fsm.context import FSMContext



router = Router()

@router.message(Command('change_fsm_to_false'))
async def change_fsm_to_false(message: Message, state: FSMContext):
    await state.update_data(used_trial_subscription=False)
    data = await state.get_data()
    data = data.get('used_trial_subscription')
    await message.answer(
        text=f'fsm is {data}'
    )

@router.message(Command('change_fsm_to_true'))
async def change_fsm_to_false(message: Message, state: FSMContext):
    await state.update_data(used_trial_subscription=True)
    data = await state.get_data()
    data = data.get('used_trial_subscription')
    await message.answer(
        text=f'fsm is {data}'
    )