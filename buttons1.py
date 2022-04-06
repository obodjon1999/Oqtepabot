from telegram import KeyboardButton,InlineKeyboardButton,InlineKeyboardMarkup
from telegram import ReplyKeyboardMarkup,InlineKeyboardMarkup
from data_tel_bot import *
button_start = [
    ['Boshlash']
]
button_phone = [
    [KeyboardButton('Raqamni yuborish', request_contact=True)]
]
button_location = [
    [KeyboardButton('Lokatsiya yuborish', request_location=True)]
]




def button_main():
    button=[]
    data=get_category()
    res=[]
    for i in data:
        res.append(InlineKeyboardButton(i[1],callback_data=f"{i[1]}_{i[0]}"))
        if len(res)==2:
            button.append(res)
            res=[]

    if len(res)>0:

        button.append(res)
    button.append([InlineKeyboardButton("? Buyurtmalar tarixi",callback_data="buyurtmalar")])
    button.append([InlineKeyboardButton(" ? Savatcha",callback_data="Savatcha")])
    return button


def button_admin_main():
    button=[]
    data=get_category()
    res=[]
    for i in data:
        res.append(i[1])
        if len(res)==2:
            button.append(res)
            res=[]

    if len(res)>0:
        button.append(res)
    return ReplyKeyboardMarkup(button)



button_lavash=[
    [InlineKeyboardButton("Lavash", callback_data="Lavash"), InlineKeyboardButton("Lavash Mini", callback_data="Lavashmini")],
    [InlineKeyboardButton("Lavash Sirli", callback_data="Lavashsirli"), InlineKeyboardButton("Tandir Lavash", callback_data="Tandirlavash")],
    [InlineKeyboardButton("Tandir Lavash Sirli", callback_data="Tandirlavashsirli"), InlineKeyboardButton("Lavash urta", callback_data="Lavashurta")],
]

def category_product_button(product):
    button=[]
    res=[]
    for i in product:
        res.append(InlineKeyboardButton(i[1],callback_data=f"{i[0]}"))
        if len(res)==2:
            button.append(res)
            res=[]
    if len(res)==1:
        button.append(res)
    return InlineKeyboardMarkup(button)

def product_soni(soni):
    button=[

        [InlineKeyboardButton(text=f"Tanlangan {soni}  ",callback_data="soni")],
        [InlineKeyboardButton("1",callback_data="1"),InlineKeyboardButton("2",callback_data="2"),InlineKeyboardButton("3",callback_data="3")],
        [InlineKeyboardButton("4",callback_data="4"),InlineKeyboardButton("5",callback_data="5"),InlineKeyboardButton("6",callback_data="6")],
        [InlineKeyboardButton("7",callback_data="7"),InlineKeyboardButton("8",callback_data="8"),InlineKeyboardButton("9",callback_data="9")],
        [InlineKeyboardButton("0",callback_data="0"),InlineKeyboardButton("?o`chirish",callback_data="delete")],
        [InlineKeyboardButton("Savatchaga joylash",callback_data="add")],
        [InlineKeyboardButton("Orqaga",callback_data="back")]



    ]
    return InlineKeyboardMarkup(button)



def savatcha_button(product):
    button=[]
    for i in product:
        button=[]
        print(product)
        for i in product:
            button.append([InlineKeyboardButton("+",callback_data=f"+_{i[0]}"),InlineKeyboardButton(f"{i[2]}",callback_data=f"productname"),InlineKeyboardButton("-",callback_data=f"-_{i[0]}")])
    button.append([InlineKeyboardButton("?Buyurtmani tasdiqlash",callback_data="confirm")])
    button.append([InlineKeyboardButton("yana buyurtma berish",callback_data="again")])
    return InlineKeyboardMarkup(button)













