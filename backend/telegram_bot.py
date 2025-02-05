# RAG-powered bot (no hallucinations!)
from telegram import Update
from telegram.ext import Application, MessageHandler, filters
from rag import get_llm_response

app = Application.builder().token("YOUR_TELEGRAM_TOKEN").build()

async def handle_message(update: Update, _):
    response = get_llm_response(update.message.text)
    await update.message.reply_text(response)

app.add_handler(MessageHandler(filters.TEXT, handle_message))
app.run_polling()
