from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup, InputFile
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes, CallbackQueryHandler

# 🛡️ Вставь сюда свой токен от BotFather
TOKEN = "7719547111:AAFEgzsV98e943mFnoPpCOj0mTma865FYhg"

# 📍 Команда /start с кнопками
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    keyboard = [
        [InlineKeyboardButton("📖 О курсе", callback_data="about")],
        [InlineKeyboardButton("📊 Пройти опрос", callback_data="poll")],
        [InlineKeyboardButton("💰 Купить курс", callback_data="buy")]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    await update.message.reply_text(
        "Привет! Я бот 'Макияж для Себя' 💄\n\nВыбери, с чего начнём 👇",
        reply_markup=reply_markup
    )

# 📊 Опрос по уровню макияжа
async def poll(update: Update, context: ContextTypes.DEFAULT_TYPE):
    question = "Какой у тебя уровень макияжа?"
    options = ["Новичок", "Знаю основы", "Любитель", "Визажист"]
    await update.effective_chat.send_poll(question=question, options=options, is_anonymous=False)

# ⌨️ Обработка кнопок
async def button_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()
    if query.data == "about":
        await query.edit_message_text("👩‍🏫 Этот курс научит тебя делать макияж для себя — просто, понятно и красиво.")
    elif query.data == "poll":
        await poll(update, context)
    elif query.data == "buy":
        await query.edit_message_text("💌 Чтобы купить курс, напиши нам: @SelfMakeupSupport или нажми кнопку ниже.")

# 🚀 Инициализация приложения
app = ApplicationBuilder().token(TOKEN).build()
app.add_handler(CommandHandler("start", start))
app.add_handler(CallbackQueryHandler(button_handler))
app.run_polling()