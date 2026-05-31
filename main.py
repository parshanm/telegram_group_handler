import asyncio
from aiogram import Bot, Dispatcher, types
from aiogram.filters import Command
from conditions import GroupChatFilter, PrivateChatFilter
from logger import LOGS

token = ''

bot = Bot(token=token)

dp = Dispatcher()

@dp.message(Command('start'))
async def start(message: types.Message):
    pass

async def main():
    LOGS.info('---Starting Bot---')
    await dp.start_polling()

if __name__ == "__main__":
    asyncio.run(main())
