import asyncio
import os

from aiogram import Bot
from apscheduler.schedulers.asyncio import AsyncIOScheduler

BOT_TOKEN = os.environ["BOT_TOKEN"]
CHANNEL_ID = int(os.environ["CHANNEL_ID"])

MESSAGE_TEXT = (
    "🔔 Напоминание!\n\n"
    "Через 5 минут начнётся конференция.\n"
    "Подключайтесь вовремя."
)

bot = Bot(token=BOT_TOKEN)

scheduler = AsyncIOScheduler(
    timezone="Asia/Almaty"
)


async def send_reminder():
    print("Отправляю напоминание...")

    await bot.send_message(
        chat_id=CHANNEL_ID,
        text=MESSAGE_TEXT
    )


def setup_scheduler():
    scheduler.add_job(
        send_reminder,
        trigger="cron",
        day_of_week="fri",
        hour=13,
        minute=20
    )

    scheduler.start()


async def main():
    setup_scheduler()

    print("Бот запущен ⏰")

    while True:
        await asyncio.sleep(3600)


if __name__ == "__main__":
    asyncio.run(main())
