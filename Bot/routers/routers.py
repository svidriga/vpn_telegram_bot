from aiogram import Router

from Bot.handlers.user import callbacks, commands, f_messages
from Bot.handlers.admin import test


def setup_routers() -> Router:
    main_router = Router()

    # user
    main_router.include_router(commands.router)
    main_router.include_router(f_messages.router)
    main_router.include_router(callbacks.router)

    # admin
    main_router.include_router(test.router)

    return main_router