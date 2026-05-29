from telegram import Update
from telegram.ext import Application, MessageHandler, filters, ContextTypes
import yt_dlp
import os

TOKEN = "TOKEN"

async def download_video(update: Update, context: ContextTypes.DEFAULT_TYPE):

    url = update.message.text

    await update.message.reply_text("در حال دانلود...")

    ydl_opts = {
        'format': 'mp4',
        'outtmpl': 'video.%(ext)s'
    }

    try:
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            info = ydl.extract_info(url, download=True)
            filename = ydl.prepare_filename(info)

        await update.message.reply_video(video=open(filename, 'rb'))

        os.remove(filename)

    except Exception:
        await update.message.reply_text("خطا در دانلود")

app = Application.builder().token(TOKEN).build()

app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, download_video))

app.run_polling()