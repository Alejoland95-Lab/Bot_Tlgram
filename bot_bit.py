import os
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters

# Leemos el TOKEN desde las variables de entorno (Railway lo pondrá)
TOKEN = os.getenv("8305414858:AAFgrm9NaLqqGGkby15aLO2VRGzgOXqcLVw")

if not TOKEN:
    raise ValueError("No se encontró el TOKEN en las variables de entorno.")

# Mensaje de bienvenida
def start(update, context):
    update.message.reply_text("Bienvenido! Envía un número entre 0 y 100.")

# Manejo de cualquier mensaje de texto
def check_number(update, context):
    try:
        num = int(update.message.text)
        if 0 <= num <= 100:
            if num == 74:
                update.message.reply_text("Felicidades número correcto")
            else:
                update.message.reply_text("Lo siento número incorrecto")
        else:
            update.message.reply_text("El número debe estar entre 0 y 100.")
    except ValueError:
        update.message.reply_text("Por favor envía un número válido.")

def main():
    updater = Updater(TOKEN, use_context=True)
    dp = updater.dispatcher

    # Comando /start
    dp.add_handler(CommandHandler("start", start))

    # Cualquier texto que no sea comando
    dp.add_handler(MessageHandler(Filters.text & ~Filters.command, check_number))

    updater.start_polling()
    updater.idle()

if __name__ == "__main__":
    main()