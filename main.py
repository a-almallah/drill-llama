import logging
import asyncio
from telegram.ext import Application, MessageHandler, filters
from config import TELEGRAM_BOT_TOKEN
import bot

logging.basicConfig(level=logging.INFO)

async def main():
    if not TELEGRAM_BOT_TOKEN:
        print("Set TELEGRAM_BOT_TOKEN")
        return

    app = Application.builder().token(TELEGRAM_BOT_TOKEN).build()
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, bot.handle_message))
    
    asyncio.create_task(bot.proactive_insult_loop(app))
    
    await app.initialize()
    await app.start()
    await app.updater.start_polling()
    
    stop_event = asyncio.Event()
    await stop_event.wait()

if __name__ == "__main__":
    asyncio.run(main())
