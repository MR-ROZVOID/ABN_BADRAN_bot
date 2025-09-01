from telegram import Update
from telegram.ext import Application, MessageHandler, filters, ContextTypes

TOKEN = "8416841364:AAH_gf08ccRuju_Fz1CLKdtdi3OItlHKOOs"

async def welcome(update: Update, context: ContextTypes.DEFAULT_TYPE):
    for member in update.message.new_chat_members:
        username = member.first_name  # أو member.username إذا تحب يظهر @username
        message = f"""👋 حياك اخي {username}
---
هذه مجموعة دردشة تحت ادارة سُنية بالكامل واحنا نرحب بالاعضاء من كل المذاهب والمعتقدات
---
عندك الحرية بالمناقشة وطرح افكارك ومعتقداتك ولكن باحترام وبدون تهجم
---
الك كامل الحق بانتقاد اي شخص في المجموعة ولكن باحترام وبدون سب
---
لاتستحي بطرح اهتماماتك وهواياتك
"""
        await update.message.reply_text(message)

app = Application.builder().token(TOKEN).build()

# الاستماع للأعضاء الجدد
app.add_handler(MessageHandler(filters.StatusUpdate.NEW_CHAT_MEMBERS, welcome))

print("البوت يعمل ...")
app.run_polling()
