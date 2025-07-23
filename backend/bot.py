from telegram import Update, KeyboardButton, ReplyKeyboardMarkup, InlineKeyboardMarkup, InlineKeyboardButton
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, ContextTypes, filters
from db import add_or_update_user
from config import BOT_TOKEN

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    keyboard = [
        [KeyboardButton("📱 Share Phone", request_contact=True)]
    ]
    reply_markup = ReplyKeyboardMarkup(keyboard, resize_keyboard=True)

    # 💡 Inline button for Web App
    web_app_keyboard = InlineKeyboardMarkup([
        [InlineKeyboardButton("🧩 Open Web App", web_app={"url": "https://xxlz3kw8-5000.asse.devtunnels.ms"})]
    ])

    await update.message.reply_text("Welcome! Please share your phone number:", reply_markup=reply_markup)
    await update.message.reply_text("Or tap below to open the Web App:", reply_markup=web_app_keyboard)

async def contact_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    contact = update.message.contact
    user = update.message.from_user

    added = add_or_update_user(
        telegram_id=str(user.id),
        name=user.full_name,
        phone_number=contact.phone_number,
        role='user'
    )

    if added:
        await update.message.reply_text(f"Thanks {user.full_name}, you’ve been registered!")
    else:
        await update.message.reply_text(f"Welcome back {user.full_name}! You're already registered.")

app = ApplicationBuilder().token(BOT_TOKEN).build()
app.add_handler(CommandHandler("start", start))
app.add_handler(MessageHandler(filters.CONTACT, contact_handler))

if __name__ == "__main__":
    app.run_polling()
