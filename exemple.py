from aiogram import Bot, Dispatcher, F
from aiogram.filters import Command, CommandStart
from aiogram.utils.keyboard import ReplyKeyboardBuilder
from aiogram.types import (
    KeyboardButton,
    Message,
    ReplyKeyboardMarkup,
    ReplyKeyboardRemove
)

bot = Bot(token="5854219374:AAF0ghjSr6ipw7BUTMHUYS9yrflGsPidNTo")
dp = Dispatcher()



choices = ["Камень", "Ножницы", "Бумага"]
yes_or_no = ['Давай!', 'Не хочу!']

users = {}

kb_builder = ReplyKeyboardBuilder()
buttons1 = [KeyboardButton(text=f"{i}") for i in yes_or_no]
kb_builder.row(*buttons1)
kb_builder2 = ReplyKeyboardBuilder()
buttons2 = [KeyboardButton(text=f"{i}") for i in choices]
kb_builder2.row(*buttons2)

@dp.message(CommandStart())
async def start_command(message: Message):
    await message.answer(text="Приветствую в игре \"Камень, Ножницы, Бумага\"",
                         reply_markup=kb_builder.as_markup(resize_keyboard=True)
                         )
    if not message.from_user.id in users:
        users[message.from_user.id] = {
            'in_game': False,
            'total_games': 0,
            'wins': 0
        }

@dp.message(F.text == (yes_or_no[0]))
async def start_command(message: Message):
    await message.answer(text=f"Твой ход:",
                         reply_markup=kb_builder2.as_markup(resize_keyboard=True))

    if not users[message.from_user.id]['in_game']:
        users[message.from_user.id]['in_game'] = True
        users[message.from_user.id]['total_games'] += 1

@dp.message(Command(commands=yes_or_no[1]))
async def start_command(message: Message):
    await message.answer(text=f"Возвращайся когдап будешь готов",
                         reply_markup=kb_builder2.as_markup(resize_keyboard=True))

    if users[message.from_user.id]['in_game']:
        users[message.from_user.id]['in_game'] = False


if __name__ == '__main__':
    dp.run_polling(bot)