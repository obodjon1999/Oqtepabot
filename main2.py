from telegram import *
from telegram.ext import Updater, CallbackContext,ConversationHandler,CommandHandler,MessageHandler,CallbackQueryHandler
from functions2 import *



conv=ConversationHandler(
    entry_points=[
        CommandHandler("start",start)
    ],
    states={
        "state_main":[
            CallbackQueryHandler(command_callback)
        ],

    },
    fallbacks=[
        CommandHandler("start",start)
    ]
)
updater = Updater('5142638177:AAF4h5utCujwWhxdlzM1jWIJHxEhF5bNzMg')
updater.dispatcher.add_handler(conv)
updater.start_polling()
updater.idle()