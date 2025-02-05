import os
from telegram import Update
from telegram.ext import ApplicationBuilder, ContextTypes, MessageHandler, filters
from rag import get_rag_response

async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    response = get_rag_response(update.message.text)
    await context.bot.send_message(
        chat_id=update.effective_chat.id, 
        text=response
    )

if _name_ == "_main_":
    app = ApplicationBuilder().token(os.getenv("TELEGRAM_TOKEN")).build()
    app.add_handler(MessageHandler(filters.TEXT, handle_message))
    app.run_polling()
