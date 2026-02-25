from telegram.ext import Updater, CommandHandler, MessageHandler, Filters


TOKEN = "TU_TOKEN_AQUI"


def start(update, context):
    update.message.reply_text("Bienvenido! Envía un número entre 0 y 100.")


def check_number(update, context):
    try:
        num = int(update.message.text)
        if num == 74:
            update.message.reply_text("🎉 Felicidades número correcto")
        else:
            update.message.reply_text("❌ Lo siento número incorrecto")
    except ValueError:
        update.message.reply_text("Por favor envía un número válido.")

def main():
    updater = Updater(TOKEN, use_context=True)
    dp = updater.dispatcher

    
    dp.add_handler(CommandHandler("start", start))

    
    dp.add_handler(MessageHandler(Filters.text & ~Filters.command, check_number))

    
    updater.start_polling()
    updater.idle()

if __name__ == "__main__":
    main()