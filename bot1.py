from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes

TOKEN = "8988007625 :AAHXiupxzxgsq4WB8k-SN5t4Yc_t7Kziois

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("سلام 👋 ربات فعاله")

app = Application.builder().token(TOKEN).build()
app.add_handler(CommandHandler("start", start))

app.run_polling()