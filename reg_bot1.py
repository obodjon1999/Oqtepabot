
from function1 import *

conv = ConversationHandler(
    entry_points=[
        CommandHandler('start', start)

    ],
    states={
        'start': [
            MessageHandler(Filters.regex('^(' + "Boshlash" + ')$'), boshlash)
        ],
        'state_name': [
            MessageHandler(Filters.text, command_name)
        ],
        'state_phone': [
            MessageHandler(Filters.contact, command_phone)
        ],
        'state_main': [
            CallbackQueryHandler(command_callback)

        ],
        'state_product':[
            CallbackQueryHandler(command_callback_product)

        ],
        state_klaviatura:[
            CallbackQueryHandler(command_klaviatura)

        ],
        'state_savatcha':[
            CallbackQueryHandler(command_savatcha)
        ],

        'state_admin':[
            MessageHandler(Filters.text,command_admin_category)

        ],
        'state_location':[
            MessageHandler(Filters.location,command_location)
        ],
        'state_admin_product':[
            MessageHandler(Filters.text,commmand_admin_product)
        ],
        'state_admin_product_price':[
            MessageHandler(Filters.text,command_admin_price)
        ],
        'state_admin_product_photo':[
            MessageHandler(Filters.photo,command_admin_image)
        ]




    },

    fallbacks=[
        CommandHandler('start', start)
    ]
)

updater = Updater('5142638177:AAF4h5utCujwWhxdlzM1jWIJHxEhF5bNzMg')

updater.dispatcher.add_handler(conv)
updater.dispatcher.add_handler(CommandHandler("addcat",command_addcat))
updater.start_polling()
updater.idle()