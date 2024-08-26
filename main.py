from typing import Final
from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, filters, ContextTypes
from datamanager import DataManager
from days import Days
from stormglass import StormGlass
import os

TOKEN: Final = os.environ.get("TOKEN")
BOT_USERNAME: Final = '@'
STORM_GLASS_API_KEY_HOTMAIL = os.environ.get("STORM_GLASS_API_KEY_HOTMAIL")
STORM_GLASS_API_KEY_GMAIL = os.environ.get("STORM_GLASS_API_KEY_GMAIL")
STORM_GLASS_API_KEY_GMAIL_TRABAJO = os.environ.get("STORM_GLASS_API_KEY_GMAIL_TRABAJO")
STORM_GLASS_API_KEY_GMAIL_FUEGOLENTO = os.environ.get("STORM_GLASS_API_KEY_GMAIL_FUEGOLENTO")
STORM_GLASS_API_KEY_GMAIL_MAMA = os.environ.get("STORM_GLASS_API_KEY_GMAIL_MAMA")
URL_STORM_GLASS_ENDPOINT = "https://api.stormglass.io/v2"

data_manager = DataManager()
storm_glass = StormGlass(STORM_GLASS_API_KEY_GMAIL_MAMA,URL_STORM_GLASS_ENDPOINT)
storm_glass_weather = StormGlass(STORM_GLASS_API_KEY_GMAIL,URL_STORM_GLASS_ENDPOINT)

async def start_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Hola, bienvenido a tu asistente de mareas. Tienes los siguientes comandos disponibles: \n  "
                          "- /today para ver la tabla de mareas de hoy en Lagos\n"
                          "- /now para saber cómo está la marea ahora mismo en Lagos\n"
                          "- /tomorrow para ver la tabla de mareas de mañana en lagos")




async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Hola, Tienes los siguientes comandos disponibles: \n  "
                          "- /today para ver la tabla de mareas de hoy en Lagos\n"
                          "- /now para saber cómo está la marea ahora mismo en Lagos\n"
                          "- /tomorrow para ver la tabla de mareas de mañana en lagos")

async def now_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    date_utils = Days()
    data = storm_glass.fetch_tide_today_lagos()
    result = data_manager.verify_tide(data, date_utils.now())
    message_to_send = f"Ahora la Marea está {result['message']['tide']}, {result['message']['extreme']} será: {result['date'].strftime('%H:%M')}"
    await update.message.reply_text(message_to_send)

async def today_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    date_utils = Days()

    all_tides = storm_glass.fetch_tide_today_lagos()
    tides = data_manager.get_correct_tides(all_tides, date_utils.now())
    data_manager.generate_graph_tide(tides, date_utils.now())
    photo = open('mareas.jpg', 'rb')

    await update.message.reply_photo(photo)

async def tomorrow_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    date_utils = Days()
    all_tides = storm_glass.fetch_tide_tomorrow()
    tides = data_manager.get_correct_tides(all_tides, date_utils.tomorrow_end())
    data_manager.generate_graph_tide(tides, Days().tomorrow_ini())
    photo = open('mareas.jpg', 'rb')
    await update.message.reply_photo(photo)


async def weather_today_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    date_utils = Days()

    weather = storm_glass.fetch_weather(date_utils.today_ini(), date_utils.tomorrow_end())
    data_manager.generate_table_weather(weather, date_utils.now())
    photo = open('tabla_tiempo.jpg', 'rb')
    await update.message.reply_photo(photo)


async def weather_tomorrow_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    date_utils = Days()
    weather = storm_glass.fetch_weather(date_utils.tomorrow_ini(), date_utils.tomorrow_end())
    data_manager.generate_table_weather(weather, date_utils.tomorrow())
    photo = open('tabla_tiempo.jpg', 'rb')
    await update.message.reply_photo(photo)


def handle_response(text: str) -> str:
    if 'today' in text:
        return 'today'

    return 'else'

async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text: str = update.message.text

    await update.message.reply_text(handle_response(text))


async def error(update:Update, context: ContextTypes.DEFAULT_TYPE):
    print(f'update: {update} caused error {context.error}')


if __name__ == '__main__':
    print('starting bot')
    app = Application.builder().token(TOKEN).build()

    app.add_handler(CommandHandler('start',start_command))
    app.add_handler(CommandHandler('help', help_command))
    app.add_handler(CommandHandler('today',today_command))
    app.add_handler(CommandHandler('now',now_command))
    app.add_handler(CommandHandler('tomorrow',tomorrow_command))
    app.add_handler(CommandHandler('weather_today',weather_today_command))
    app.add_handler(CommandHandler('weather_tomorrow',weather_tomorrow_command))

    app.add_error_handler(error)

    print('polling')
    app.run_polling(poll_interval=3)