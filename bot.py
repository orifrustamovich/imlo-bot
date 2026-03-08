import asyncio
import logging
import sys

from dotenv import load_dotenv
from os import getenv

from aiogram import Bot, Dispatcher, html
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode
from aiogram.filters import CommandStart, Command
from aiogram.types import Message

from checkWord import checkWord

load_dotenv()

# Bot token can be obtained via https://t.me/BotFather
TOKEN = getenv("BOT_TOKEN")

# All handlers should be attached to the Router (or Dispatcher)

dp = Dispatcher()


@dp.message(CommandStart())
async def command_start_handler(message: Message) -> None:
    await message.answer(f"Assalomu alaykum! {html.bold(message.from_user.full_name)} imlo botiga xush kelibsiz! \n So'z kiriting:")


@dp.message(Command("help"))
async def command_help_handler(message: Message) -> None:

    await message.answer(f"Bu so'zlarning imlo xatolarini topuvchi bot! \n So'z kiriting:")


@dp.message()
async def echo_handler(message: Message) -> None:
    # try:
    #     await message.send_copy(chat_id=message.chat.id)
    # except TypeError:
    #     await message.answer("Nice try!")

    word = message.text
    result = checkWord(word)
    if result['available']:
        response = f"✅ {word.capitalize()}"
    else:
        response = f"❌ {word.capitalize()}\n"
        for text in result['matches']:
            response += f"✅ {text.capitalize()}\n"
    await message.answer(response)


async def main() -> None:
    # Initialize Bot instance with default bot properties which will be passed to all API calls
    bot = Bot(token=TOKEN, default=DefaultBotProperties(parse_mode=ParseMode.HTML))

    # And the run events dispatching
    await dp.start_polling(bot)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    asyncio.run(main())