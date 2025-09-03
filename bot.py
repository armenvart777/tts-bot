"""
TTS Bot - Text to Speech через ElevenLabs
Отправляешь текст на немецком → получаешь голосовое сообщение
"""

import os
import logging
import tempfile
import asyncio

from aiogram import Bot, Dispatcher, F
from aiogram.types import Message, FSInputFile
from aiogram.filters import CommandStart, Command
from aiogram.enums import ChatAction

import aiohttp

logging.basicConfig(level=logging.INFO, format='%(asctime)s [%(levelname)s] %(message)s')
logger = logging.getLogger(__name__)

BOT_TOKEN = os.getenv("BOT_TOKEN")
ELEVENLABS_API_KEY = os.getenv("ELEVENLABS_API_KEY")

# Немецкий голос по умолчанию (можно поменять)
# Daniel - мужской немецкий голос
VOICE_ID = os.getenv("VOICE_ID", "onwK4e9ZLuTAKqWW03F9")

ELEVENLABS_URL = f"https://api.elevenlabs.io/v1/text-to-speech/{VOICE_ID}"

bot = Bot(token=BOT_TOKEN)
dp = Dispatcher()


async def generate_speech(text: str) -> bytes | None:
    """Генерирует аудио через ElevenLabs API."""
    ...


@dp.message(CommandStart())
async def cmd_start(message: Message):
    ...


@dp.message(Command("voice"))
async def cmd_voice(message: Message):
    ...


@dp.message(Command("voices"))
async def cmd_voices(message: Message):
    """Список немецких голосов."""
    ...


@dp.message(Command("setvoice"))
async def cmd_setvoice(message: Message):
    """Сменить голос."""
    ...


@dp.message(F.text)
async def handle_text(message: Message):
    """Генерирует голосовое из текста."""
    ...


async def main():
    logger.info("TTS Bot started")
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())
