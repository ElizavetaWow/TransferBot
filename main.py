import asyncio
import logging
import pathlib
import os
from aiogram import Bot, Dispatcher, types
from aiogram.utils.markdown import text, bold
from aiogram.types import ParseMode
from aiogram.types.message import ContentType
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup


token = pathlib.Path('token.txt').read_text()

logging.basicConfig(level=logging.INFO)
bot = Bot(token=token)
storage = MemoryStorage()
dp = Dispatcher(bot, storage=storage)
cur_path = os.getcwd()

# общие команды


@dp.message_handler(commands=['start'])
async def cmd_start(message: types.Message):
    await message.answer("Приветствую Вас в боте переноса стиля! \n\nСправку по командам можно посмотреть так /help")


@dp.message_handler(commands=['help'])
async def cmd_help(message: types.Message):
    msg = text(bold('Я могу ответить на следующие команды:'),
               '/photo - загрузка фотографии и желаемого стиля', '/cancel - отмена операции', '/help - справка по работе бота', sep='\n')
    await message.answer(msg, parse_mode=ParseMode.MARKDOWN)


@dp.message_handler(commands=['cancel'], state='*')
async def cmd_cancel(message: types.Message, state: FSMContext):
    await state.finish()
    await message.answer("Действие отменено")

# работа с фото


class GetImage(StatesGroup):
    image = State()
    style = State()


@dp.message_handler(commands=['photo'], state='*')
async def cmd_photo(message: types.Message, state: FSMContext):
    await message.answer('Загрузите фото для изменения!')
    await state.set_state(GetImage.image.state)


@dp.message_handler(state=GetImage.image, content_types=['photo'])
async def process_photo(message: types.Message, state: FSMContext):
    destination_file = cur_path + "\photos\content.jpg"
    await message.photo[-1].download(destination_file=destination_file)
    await message.answer('Загрузите фото стиля!')
    await state.set_state(GetImage.style.state)


@dp.message_handler(state=GetImage.style, content_types=['photo'])
async def process_photo(message: types.Message, state: FSMContext):
    destination_file = cur_path + "\photos\style.jpg"
    await message.photo[-1].download(destination_file=destination_file)
    await message.answer('Все фото загружены!')
    await bot.send_photo(chat_id=message.from_user.id, photo=message.photo[-1].file_id)
    await state.finish()


@dp.message_handler(content_types=ContentType.ANY)
async def unknown_message(msg: types.Message):
    message_text = text(
        'Я не знаю, что с этим делать \n Посмотрите доступные действия по команде /help')
    await msg.reply(message_text, parse_mode=ParseMode.MARKDOWN)


async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
