from telegram import *
from telegram.ext import CallbackContext
from buttons2 import *


def start(update:Update,context:CallbackContext):
    update.message.reply_photo(open("image.jpg","rb"),caption="yetqazib berish xizmati Toshkent shaxrida 10:00 dan 3:00 gacha")
    update.message.reply_text("Buyurtmani birga joylashtiramizmi ?",reply_markup=InlineKeyboardMarkup(button_main))
    return "state_main"

def command_callback(update:Update,context:CallbackContext):
    query=update.callback_query
    data=query.data
    query.message.delete()
    if data=="Lavash":
        query.message.reply_photo(open("lavash.jpg","rb"),caption="bolimi:Lavash",reply_markup=InlineKeyboardMarkup(button_lavash))

    return "state_main"

