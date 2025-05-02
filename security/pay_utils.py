import hashlib
import urllib.parse
from decouple import config
from django.urls import reverse
from .models import *
from tshaweb import settings


def generateSignature(dataArray, passPhrase = ''):
    payload = ""
    for key in dataArray:
        # Get all the data from Payfast and prepare parameter string
        payload += key + "=" + urllib.parse.quote_plus(dataArray[key].replace("+", " ")) + "&"
    # After looping through, cut the last & or append your passphrase
    payload = payload[:-1]
    if passPhrase != '':
        payload += f"&passphrase={passPhrase}"
    return hashlib.md5(payload.encode()).hexdigest()

def get_data_validate(request, order_number, order_total, id):
    SANDBOX_MODE = settings.DEBUG

    pfData = {
        "merchant_id": settings.PAYFAST_SANDBOX_MERCHANT_ID if SANDBOX_MODE else settings.PAYFAST_MERCHANT_ID,
        "merchant_key": settings.PAYFAST_SANDBOX_MERCHANT_KEY if SANDBOX_MODE else settings.PAYFAST_MERCHANT_KEY,
        "return_url":  "https://" + request.META['HTTP_HOST'] +  str(reverse('before', args=[id])),
        "cancel_url":  "https://" + request.META['HTTP_HOST'] + str(reverse("canceled", args=[id])) ,
        # "return_url": request.scheme + "://" + request.META['HTTP_HOST'] + str(reverse("done")),
        # "cancel_url": request.scheme + "://" + request.META['HTTP_HOST'] + str(reverse("canceled")),
        # "notify_url": "https://www.example.com/notify_url",
        "m_payment_id": str(order_number),
        "amount": str(order_total),
        "item_name": f"Church Donation No: {order_number}"
    }


    # passPhrase = 'jt7NOE43FZPn'
    passPhrase = ''
    signature = generateSignature(pfData, passPhrase)
    pfData['signature'] = signature



    # If in testing mode make use of either sandbox.payfast.co.za or www.payfast.co.za
    # SANDBOX_MODE = True
    pfHost = 'sandbox.payfast.co.za' if SANDBOX_MODE else 'www.payfast.co.za'


    htmlForm = f'<form action="https://{pfHost}/eng/process" method="post">'
    for key in pfData:
        htmlForm += f'<input name="{key}"  type="hidden" value="{pfData[key]}" />'

    htmlForm += '<input type="submit" class="btn-buy" value="Pay Now" /></form>'

    return htmlForm


