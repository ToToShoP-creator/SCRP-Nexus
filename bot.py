import asyncio
import logging
import sys
from aiogram import Bot, Dispatcher, F, html
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode
from aiogram.filters import CommandStart
from aiogram.types import Message, CallbackQuery, InlineKeyboardMarkup, InlineKeyboardButton

# Дані вашого нового бота SCRP-Nexus
TOKEN = "9236187437:AAHBq3im6TITQFVc_G9Wyg8l4acZZi_0wNA"

# Ініціалізація диспетчера та бота
dp = Dispatcher()

# Стильна головна клавіатура
def get_main_keyboard():
    return InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton(text="🎬 Генератор ідей", callback_data="gen_idea"),
                InlineKeyboardButton(text="🌐 Відкрити сайт Nexus", url="https://totoshop-creator.github.io/SCRP-Nexus/")
            ],
            [
                InlineKeyboardButton(text="✍️ Формат тексту", callback_data="format_help"),
                InlineKeyboardButton(text="ℹ️ Про систему", callback_data="about")
            ]
        ]
    )

@dp.message(CommandStart())
async def command_start_handler(message: Message) -> None:
    user_name = html.quote(message.from_user.full_name)
    await message.answer(
        f"⚡ **Привіт, {user_name}! Ласкаво просимо до SCRP-Nexus Hub.** 🚀\n\n"
        f"Це офіційний помічник платформи для контент-мейкерів та стрімерів.\n"
        f"Оберіть потрібну функцію за допомогою меню нижче:",
        reply_markup=get_main_keyboard()
    )

# Генератор ідей прямо в боті
@dp.callback_query(F.data == "gen_idea")
async def idea_callback(callback: CallbackQuery) -> None:
    ideas = [
        "🔥 Розпакування рідкісного тактичного спорядження з кастомним тюнінгом.",
        "🎬 ТОП-3 помилки при монтажі відео в CapCut, яких слід уникати.",
        "⚙️ Як налаштувати автоматичні сповіщення для стріму за 5 хвилин.",
        "💡 Огляд саморобного неонового нічника в постапокаліптичному стилі."
    ]
    import random
    selected = random.choice(ideas)
    await callback.message.answer(
        f"💡 **Згенерована ідея для вашого контенту:**\n\n{selected}",
        reply_markup=get_main_keyboard()
    )
    await callback.answer()

# Довідка по форматуванню
@dp.callback_query(F.data == "format_help")
async def format_callback(callback: CallbackQuery) -> None:
    await callback.message.answer(
        "✍️ **Швидке форматування для Telegram:**\n\n"
        "• Жирний: `**текст**`\n"
        "• Курсив: `*текст*`\n"
        "• Моноширинний: `` `текст` ``\n\n"
        "Скористайтеся повним набором інструментів на нашому [вебсайті](https://totoshop-creator.github.io/SCRP-Nexus/).",
        reply_markup=get_main_keyboard()
    )
    await callback.answer()

# Про систему
@dp.callback_query(F.data == "about")
async def about_callback(callback: CallbackQuery) -> None:
    await callback.message.answer(
        "⚡ **SCRP-Nexus Ecosystem**\n\n"
        "Єдина платформа утиліт, створена для автоматизації роботи та творчості.\n"
        "• Статус: Активний та автономний\n"
        "• Вебсайт: GitHub Pages",
        reply_markup=get_main_keyboard()
    )
    await callback.answer()

async def main() -> None:
    bot = Bot(token=TOKEN, default=DefaultBotProperties(parse_mode=ParseMode.HTML))
    await dp.start_polling(bot)

if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    asyncio.run(main())
