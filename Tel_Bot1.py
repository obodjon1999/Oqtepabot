from telegram import Update,ReplyKeyboardMarkup
from telegram.ext import Updater, CommandHandler, CallbackContext,MessageHandler,Filters
button=[
    ['viloyatlar'],
    ['Maydoni','Aholisi'],
    ['developer']
]


def start(update:Update,context:CallbackContext):

    update.message.reply_text(f'Assalomu alekum {update.effective_user.first_name}',
                              reply_markup=ReplyKeyboardMarkup(button,resize_keyboard=True))
    context.bot.send_message(chat_id=867748798, text=f"Sizning botingizga yangi foydalanuchi tashrif buyurdi uning ismi: {update.message.chat.first_name}")

def info(update,context):
    update.message.reply_text('bu bot sizga yaqindan yordam beradi')


def replay_text(update,context):
    text=update.message.text
    if text=="learn_python":
        update.message.reply_text('siz togri kalit sozni kiritdingiz')
    else:
        update.message.reply_text(text)



def hand_text(update,context):
    print(update.message.chat.id)
    text=update.message.text

    if text=='viloyatlar':
        update.message.reply_text("""O`zbekistonda 12 ta viloyat bor:
        1.Toshkent
        2.Sirdaryo
        3.Jizzax
        4.Samarqand
        5.Navoiy
        6.Buxoro""")
    elif text=='Maydoni':
        update.message.reply_text('Ozbekistonnning maydoni 384 000 km.kv ga teng:')
    elif text=='Aholisi':
        update.message.reply_text('35.5 mln ga yaqin aholisi mavjud hozirda')
    elif text=="developer":
        update.message.reply_text("biz sizga yaqindan yordam beramiz")
    else:
        update.message.reply_text(text)

def copm_google(update,context):
    update.message.reply_text("bu kampaniya dunyodagi eng rivojlangan kampaniyalardan biri"
                              "biz google orqali istalgan malumotlarni topaolamiz va"
                              "bu kompaniya dunyodagi yetakchi kompaniyalardan biri hisoblanadi"
                              "google kampaniyasida dunyoning turli davlatlaridan "
                              "dasturchilar kelib manawu kampaniya da ish faoliyatini yuritadi")


updater = Updater('5142638177:AAF4h5utCujwWhxdlzM1jWIJHxEhF5bNzMg')


updater.dispatcher.add_handler(CommandHandler('comp_google',copm_google))

updater.dispatcher.add_handler(CommandHandler('info',info))


updater.dispatcher.add_handler(CommandHandler('start',start))

updater.dispatcher.add_handler(MessageHandler(Filters.text,hand_text))
updater.dispatcher.add_handler(MessageHandler(Filters.text,replay_text))

updater.start_polling()
updater.idle()



