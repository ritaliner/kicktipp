#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Simple Bot to reply to Telegram messages.
This program is dedicated to the public domain under the CC0 license.
This Bot uses the Updater class to handle the bot.
First, a few handler functions are defined. Then, those functions are passed to
the Dispatcher and registered at their respective places.
Then, the bot is started and runs until we press Ctrl-C on the command line.
Usage:
Basic Echobot example, repeats messages.
Press Ctrl-C on the command line or send a signal to the process to stop the
bot.
"""

from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
import logging
import kicktipp

text = []

# Enable logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)

logger = logging.getLogger(__name__)

def rangliste(bot, update):
    #Send rangliste
    text = kicktipp.get_data()
    update.message.reply_text(text)

def von(bot, update):
    #Send rangliste
    text = "Gemacht mit Liebe von Dennis & Jasper"
    update.message.reply_text(text)
    
def schwul(bot, update):
    #Send rangliste
    text = "#nohomo"
    update.message.reply_text(text)

def bezahlt(bot, update):
    text = "Error! Nur Geiz gefunden"
    update.message.reply_text(text)
    
def aktuell(bot, update):
    #Send rangliste
    text = kicktipp.get_akt()
    update.message.reply_text(text)    
     
def error(bot, update, error):
    """Log Errors caused by Updates."""
    logger.warning('Update "%s" caused error "%s"', update, error)


def main():
    """Start the bot."""
    # Create the EventHandler and pass it your bot's token.
    updater = Updater("618070298:AAFiESoaLWVTvM151CGFGBgvaxnOPB1yOzo")

    # Get the dispatcher to register handlers
    dp = updater.dispatcher

    # on different commands - answer in Telegram
    dp.add_handler(CommandHandler("rangliste", rangliste))
    dp.add_handler(CommandHandler("von", von))
    dp.add_handler(CommandHandler("schwul", schwul))
    dp.add_handler(CommandHandler("aktuell", aktuell))
    dp.add_handler(CommandHandler("bezahlt", bezahlt))
    
    # log all errors
    dp.add_error_handler(error)

    # Start the Bot
    updater.start_polling()

    # Run the bot until you press Ctrl-C or the process receives SIGINT,
    # SIGTERM or SIGABRT. This should be used most of the time, since
    # start_polling() is non-blocking and will stop the bot gracefully.
    updater.idle()


if __name__ == '__main__':
    main()
