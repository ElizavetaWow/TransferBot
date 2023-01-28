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
from model import *


model_dict = torch.load('pretrained.model')
model_dict_clone = model_dict.copy()
for key, value in model_dict_clone.items():
    if key.endswith(('running_mean', 'running_var')):
        del model_dict[key]

style_model = Net(ngf=128)
style_model.load_state_dict(model_dict, False)

token = pathlib.Path('token.txt').read_text()

logging.basicConfig(level=logging.INFO)
bot = Bot(token=token)
storage = MemoryStorage()
dp = Dispatcher(bot, storage=storage)
cur_path = os.getcwd()
# общие команды


@dp.message_handler(commands=['start'])
async def cmd_start(message: types.Message):
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    buttons = ["Загрузить фото для обработки", "Отменить операцию", "Помощь"]
    for b in buttons:
        keyboard.add(b)

    await message.answer("Приветствую Вас в боте переноса стиля! \n\nСправку по командам можно посмотреть так /help", reply_markup=keyboard)


@dp.message_handler(lambda message: message.text == "Помощь")
@dp.message_handler(commands=['help'])
async def cmd_help(message: types.Message):
    msg = text(bold('Я могу ответить на следующие команды:'),
               '/transfer - загрузка фотографии и желаемого стиля', '/cancel - отмена операции', '/help - справка по работе бота', sep='\n')
    await message.answer(msg, parse_mode=ParseMode.MARKDOWN)


@dp.message_handler(lambda message: message.text == "Отменить операцию")
@dp.message_handler(commands=['cancel'], state='*')
async def cmd_cancel(message: types.Message, state: FSMContext):
    await state.finish()
    await message.answer("Действие отменено")

# работа с фото


class GetImage(StatesGroup):
    image = State()
    style = State()


@dp.message_handler(lambda message: message.text == "Загрузить фото для обработки")
@dp.message_handler(commands=['transfer'], state='*')
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
    await message.answer('Все фото загружены! \nМне потребуется немного времени для обработки, подождите, пожалуйста!')
    await state.finish()

    image_size = 400
    transform(style_model, cur_path + "\photos\content.jpg",
              cur_path + "\photos\style.jpg", image_size, filename=cur_path +'\photos\\result.jpg')
    with open(cur_path +'\photos\\result.jpg', 'rb') as file:
        await message.answer_photo(file, caption='Готово!')


@dp.message_handler(content_types=ContentType.ANY)
async def unknown_message(msg: types.Message):
    message_text = text(
        'Я не знаю, что с этим делать \nПосмотрите доступные действия по команде /help')
    await msg.reply(message_text, parse_mode=ParseMode.MARKDOWN)


async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
