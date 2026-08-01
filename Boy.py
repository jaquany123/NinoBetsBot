import os
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

BOT_TOKEN = os.getenv("BOT_TOKEN")
OWNER_ID = 7660744882

async def nba(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if update.effective_user.id != OWNER_ID:
        await update.message.reply_text("You are not authorized.")
        return

    pick = " ".join(context.args)

    if not pick:
        await update.message.reply_text(
            "Example:\n/nba Lakers -4.5"
        )
        return

    await update.message.reply_text(
        f"""🏀 Today's Pick

{pick}

Confidence: ⭐⭐⭐⭐

Good luck 🍀"""
    )

app = ApplicationBuilder().token(BOT_TOKEN).build()
app.add_handler(CommandHandler("nba", nba))

print("Bot is running...")
app.run_polling()
