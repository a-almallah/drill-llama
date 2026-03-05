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
    chat_history.append(f"User: {text}")
    if len(chat_history) > 5:
        chat_history.pop(0)
    
    context_text = "\n".join(chat_history)
    response = await llm.generate_insult(context_text)
    
    chat_history.append(f"Coach: {response}")
    if len(chat_history) > 5:
        chat_history.pop(0)
        
    await update.message.reply_text(response)

async def proactive_insult_loop(app):
    while True:
        await asyncio.sleep(2)
        try:
            response = await llm.generate_proactive_insult()
            await app.bot.send_message(chat_id=ALLOWED_USER_ID, text=response)
        except Exception as e:
            print(f"Failed to send proactive message: {e}")
