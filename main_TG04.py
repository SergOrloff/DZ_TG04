import logging
import os
from aiogram import Bot, Dispatcher, types
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton, BotCommand
from aiogram.filters import Command
from aiogram.fsm.storage.memory import MemoryStorage
from aiogram import Router
from dotenv import load_dotenv

# Загружаем переменные окружения из файла .env
load_dotenv()

# Получаем значения из .env файла
API_TOKEN = os.getenv('TELEGRAM_TOKEN')

# Configure logging
logging.basicConfig(level=logging.INFO)

# Initialize bot and dispatcher
bot = Bot(token=API_TOKEN)
dp = Dispatcher(storage=MemoryStorage())

# Create a router
router = Router()

# Задание 1: Создание простого меню с кнопками
@router.message(Command('start'))
async def send_welcome(message: types.Message):
    keyboard = ReplyKeyboardMarkup(
        keyboard=[
            [KeyboardButton(text="Привет")],
            [KeyboardButton(text="Пока")]
        ],
        resize_keyboard=True
    )
    await message.answer("Выберите опцию:", reply_markup=keyboard)

@router.message(lambda message: message.text in ["Привет", "Пока"])
async def handle_message(message: types.Message):
    if message.text == "Привет":
        await message.answer(f"Привет, {message.from_user.first_name}!")
    elif message.text == "Пока":
        await message.answer(f"До свидания, {message.from_user.first_name}!")

# Задание 2: Кнопки с URL-ссылками
@router.message(Command('links'))
async def send_links(message: types.Message):
    inline_keyboard = InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text="Новости", url="https://news.ycombinator.com/")],
        [InlineKeyboardButton(text="Музыка", url="https://music.yandex.ru/home")],
        [InlineKeyboardButton(text="Видео", url="https://www.youtube.com/")]
    ])
    await message.answer("Выберите ссылку:", reply_markup=inline_keyboard)

# Задание 3: Динамическое изменение клавиатуры
@router.message(Command('dynamic'))
async def send_dynamic(message: types.Message):
    inline_keyboard = InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text="Показать больше", callback_data="show_more")]
    ])
    await message.answer("Нажмите кнопку ниже:", reply_markup=inline_keyboard)

@router.callback_query(lambda callback_query: callback_query.data == 'show_more')
async def show_more_options(callback_query: types.CallbackQuery):
    inline_keyboard = InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text="Опция 1", callback_data="option_1")],
        [InlineKeyboardButton(text="Опция 2", callback_data="option_2")]
    ])
    await callback_query.message.edit_text("Выберите опцию:", reply_markup=inline_keyboard)

@router.callback_query(lambda callback_query: callback_query.data.startswith('option_'))
async def handle_options(callback_query: types.CallbackQuery):
    option = callback_query.data.split('_')[1]
    await callback_query.message.answer(f"Вы выбрали Опция {option}")

# Register router in dispatcher
dp.include_router(router)

# Функция для установки команд меню
async def set_commands(bot: Bot):
    commands = [
        BotCommand(command="start", description="Запустить бота"),
        BotCommand(command="help", description="Помощь по использованию бота"),
        BotCommand(command="links", description="Показать ссылки на новости, музыку и видео"),
        BotCommand(command="dynamic", description="Показать динамическое меню")
    ]
    await bot.set_my_commands(commands)

@dp.message(Command(commands=["help"]))
async def help_command(message: types.Message):
    await message.answer(
        "Я - Ваш гид по меню с кнопками и динамическим взаимодействием. \n"
        "Используйте команды /start для приветствия, /links для ссылок на новости, музыку и видео"
        " и /dynamic для интерактивных опций.\n"
        "*Команды:*\n"
        "/start - Запустить бота\n"
        "/help - показать эту справку\n"
        "/links - Показать ссылки на новости, музыку и видео\n"
        "/dynamic - Показать динамическое меню"
    )



# Start polling
if __name__ == '__main__':
    dp.startup.register(set_commands)
    dp.run_polling(bot)
