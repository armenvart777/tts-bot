# TTS Bot

Телеграм-бот, который принимает текст и возвращает голосовое сообщение. Синтез речи через ElevenLabs API. Изначально делался под немецкий язык, но модель `eleven_multilingual_v2` поддерживает большинство языков.

## Что умеет

- Принимает текст, отправляет голосовое сообщение (OGG OPUS)
- Если ffmpeg недоступен - отправляет MP3 как аудио
- Можно менять голос через `/setvoice <voice_id>`
- Поддерживает SSML-паузы: `<break time="1s"/>`

## Команды

- `/start` - приветствие и список возможностей
- `/voice` - показать текущий голос
- `/voices` - список популярных немецких голосов
- `/setvoice <id>` - сменить голос

## Установка

```bash
git clone https://github.com/armenvart777/tts-bot.git
cd tts-bot
pip install -r requirements.txt
cp .env.example .env
# Заполнить .env своими ключами
python bot.py
```

## Зависимости

- Python 3.10+
- ffmpeg (для конвертации MP3 в OGG, опционально)
- Токен Telegram-бота (@BotFather)
- API-ключ ElevenLabs

## Настройка .env

```
BOT_TOKEN=токен_бота
ELEVENLABS_API_KEY=ключ_elevenlabs
VOICE_ID=onwK4e9ZLuTAKqWW03F9
```

Полный список голосов и их ID - на [elevenlabs.io](https://elevenlabs.io).

## Лицензия

MIT

## Примечания

- По умолчанию используется немецкий голос Daniel
- Максимальная длина текста зависит от плана ElevenLabs
