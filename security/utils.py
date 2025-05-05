import datetime
import math
import random
from uuid import uuid4


def order_num_gen():
    return _generate_cart_id().upper()
# def order_num_gen():
#     id = None
#     yr = int(datetime.date.today().strftime("%Y"))
#     dt = int(datetime.date.today().strftime("%d"))
#     mt = int(datetime.date.today().strftime("%m"))
#     d = datetime.date(yr,mt,dt)
#     current_date = d.strftime("%Y%m%d")

#     order_nun = str(current_date) + str(id)
#     return order_nun

def new_payment_id(id):
    
    yr = int(datetime.date.today().strftime("%Y"))
    dt = int(datetime.date.today().strftime("%d"))
    mt = int(datetime.date.today().strftime("%m"))
    d = datetime.date(yr,mt,dt)
    current_date = d.strftime("%Y%m%d")

    order_nun = str(current_date) + str(id)
    return order_nun
    
numb = "1234567890"
alph = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

ass = numb * 9 + alph

def order_num_generator(id, n=12):
    dt = len(str(id))
    key = ""
    for j in range(n-dt):
        k = random.randint(0, len(ass)-2)
        key += ass[k]
    return key + str(id)


SHIPPING_FEE_PER_COUNTRY = 100
def _generate_cart_id():
    cart_id = ""
    characters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz1234567890'.lower() #()!*$#%&^@
    cart_id_length = 50
    c_length = len(characters)

    digits = "0123456789"
    OTP = ""
    for i in range(13) :
        OTP += characters[math.floor(random.random() * c_length)]
    return OTP


def convert_now(from_currency, to_currency, amount):
    # try:
    #     from forex_python.converter import CurrencyRates

    #     cr = CurrencyRates()

        # amount = int(input("Please enter the amount you want to convert: "))

        # from_currency = input("Please enter the currency code that has to be converted: ").upper()

        # to_currency = input("Please enter the currency code to convert: ").upper()

        # print("You are converting", amount, from_currency, "to", to_currency,".")

        # output = cr.convert(from_currency, to_currency, amount)

    # except:
    output = float(amount)/15.5

    # print("The converted rate is:", output)
    return output