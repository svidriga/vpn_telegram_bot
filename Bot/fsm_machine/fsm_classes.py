from aiogram.fsm.state import State, StatesGroup

class TrialStatus(StatesGroup):
    used_trial_subscription = State()