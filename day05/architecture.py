from aiogram import Bot, Dispatcher, Router


dp = Dispatcher()
router = Router()

dp.include_router(router)

print("Router connected successfully")