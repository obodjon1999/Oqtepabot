from telegram import Update,ReplyKeyboardMarkup,KeyboardButton
from telegram.ext import Updater, CommandHandler, CallbackContext,MessageHandler,Filters,ConversationHandler
from data_tel_bot import *
button_start=[
    ["Boshlash"],
]
button_phone=[
    [KeyboardButton('Raqamni yuborish',request_contact=True)]
]
main_button=[
    ['Taomlar'],
    ['Desert','Ichimliklar'],
    ['Dasturchi']
]
def Start(Update:Update,context:CallbackContext):
    chek=check_users(Update.effective_user.id)
    if chek:
        Update.message.reply_text("Botimizga xush kelibsiz",reply_markup=ReplyKeyboardMarkup(main_button,resize_keyboard=True))
        return "state_main"
    else:
        Update.message.reply_html(f"Asssalomu alekum <b>{Update.effective_user.first_name}, {Update.effective_user.last_name}</b>\n"
                                  f"Botimizga xush kelibsiz.Botdan foydalanish un siz royhatdan utishingiz kk",reply_markup=ReplyKeyboardMarkup(button_start,resize_keyboard=True))

    return "Start"
def boshlash(update:Update,context:CallbackContext):
    button=[
        [f'{update.effective_user.last_name} {update.effective_user.first_name}']
    ]

    update.message.reply_text("Registratsiya jarayoni boshlandi\n"
                              "Ismi familiyangizni toliq kiriting",reply_markup=ReplyKeyboardMarkup(button,resize_keyboard=True))
    return "state_main"
def command_name(update:Update,context:CallbackContext):
    text=update.message.text
    print(text)
    context.user_data['name']=text
    update.message.reply_html("telefon raqamingizni kiriting",reply_markup=ReplyKeyboardMarkup(button_phone,resize_keyboard=True))
    return "state_phone"
def command_phone(update:Update,context:CallbackContext):
    phone_nomer=update.message.contact.phone_number
    full_name=context.user_data['name']
    telegram_id=update.effective_user.id
    add_users(full_name,phone_nomer,telegram_id)
    update.message.reply_text("siz royhatdan muaffaqqiyatli otdingiz",reply_markup=ReplyKeyboardMarkup(main_button,resize_keyboard=True))
    return "state_main"
def command_taomlar_main(update:Update,context:CallbackContext):
    update.message.reply_photo(photo=open("lavash.jpg","rb"),caption="rasmlar menyusi")
    update.message.reply_text("siz taomlar menyusini tanladingiz")

def command_desert_main(update:Update,context:CallbackContext):
    update.message.reply_text("siz taomlar menyusini tanladingiz")

def command_ichimliklar_main(update:Update,context:CallbackContext):
    update.message.reply_text("siz taomlar menyusini tanladingiz")

def command_dasturchi_main(update:Update,context:CallbackContext):
    update.message.reply_text("siz taomlar menyusini tanladingiz")


conv=ConversationHandler(
    entry_points=[
        CommandHandler('start',Start)
    ],
    states={
        "Start":[
          MessageHandler(Filters.regex('^('+"Boshlash"+')$'),boshlash)
        ],
        "state_name":[
            MessageHandler(Filters.text,command_name)
        ],
        "state_phone":[
            MessageHandler(Filters.contact,command_phone)
        ],
        "state_main":[
          MessageHandler(Filters.regex('^('+"Taomlar"+')$'),command_taomlar_main),
          MessageHandler(Filters.regex('^('+"Desert"+')$'),command_desert_main),
          MessageHandler(Filters.regex('^('+"Ichimliklar"+')$'),command_ichimliklar_main),
          MessageHandler(Filters.regex('^('+"Dasturchi"+')$'),command_dasturchi_main)


        ],

    },
    fallbacks=[

        CommandHandler('satrt',Start)
    ]
)
updater = Updater('5142638177:AAF4h5utCujwWhxdlzM1jWIJHxEhF5bNzMg')

updater.dispatcher.add_handler(conv)
updater.start_polling()
updater.idle()


