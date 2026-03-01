import random
import asyncio
from telegram import Update
from telegram.ext import ContextTypes
import llm
from config import ALLOWED_USER_ID

chat_history = []

async def check_user(update: Update) -> bool:
    if update.effective_user.id != ALLOWED_USER_ID:
        await update.message.reply_text("Who are you? Go away.")
        return False
    return True

async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if not await check_user(update): return
    
    text = update.message.text
    response = await llm.generate_insult(text)
    await update.message.reply_text(response)
