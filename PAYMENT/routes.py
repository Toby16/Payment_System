from LURA import app
from fastapi import status, Depends, HTTPException, Form

from LURA.models import (User)
from LURA.helper import (
    email_validator, generate_token,
    decode_jwt, get_token, get_json_,
    write_json_, encrypt_
)
from PAYMENT.pydantic_models import (
    flutterwave_payment_pydantic_model,
    flutterwave_card_payment_pydantic_model,
    flutterwave_model, page_search_model,
    paystack_model, verify_paystack_payment_model
)


import time
import os
import re
import httpx
from httpx import Timeout
from random import randint



# [ PAYSTACK PAYMENT ]
PAYSTACK_SECRET_KEY = os.getenv("PAYSTACK_SECRET_KEY")
PAYSTACK_BASE_URL = "https://api.paystack.co/transaction"

per_dollar = 1400

@app.post("/payment/paystack", status_code=status.HTTP_200_OK, tags=["PAYMENT"])
@app.post("/payment/paystack/", status_code=status.HTTP_200_OK, tags=["PAYMENT"])
def create_payment_paystack(data: paystack_model):
    headers = {
        "Authorization": f"Bearer {PAYSTACK_SECRET_KEY}",
        "Content-Type": "application/json"
    }

    data = data.dict()

    # paystack payment payload
    payload = {
        "amount": str(int(data["amount"]) * 100),
        "email": data["email"],
        "currency": data["currency"]
        "callback_url": data["redirect_url"]
    }

    try:
        with httpx.Client(timeout=Timeout(50.0)) as client:
            # set timeout to 30 seconds
            response = client.post(f"{PAYSTACK_BASE_URL}/initialize", json=payload, headers=headers)
    except httpx.TimeoutException as e:
        raise HTTPException(status_code=500, detail=str(e))
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

    if response.status_code != 200:
        raise HTTPException(status_code=response.status_code, detail=response.json())
  
    return {
        "statusCode": 200,
        "message": "Payment created successfully",
        "response": response.json()
    }

# [ VERIFY PAYSTACK PAYMENT ]
@app.post("/payment/paystack/verify", status_code=status.HTTP_200_OK, tags=["PAYMENT"])
@app.post("/payment/paystack/verify/", status_code=status.HTTP_200_OK, tags=["PAYMENT"])
def verify_paystack_payment(data: verify_paystack_payment_model):
    headers = {
        "Authorization": f"Bearer {PAYSTACK_SECRET_KEY}"
    }

    data = data.dict()

    # paystack payment payload
    payload = {
        "reference": data["reference"]
    }

    try:
        with httpx.Client(timeout=Timeout(50.0)) as client:
            # set timeout to 30 seconds
            response = client.get(f"{PAYSTACK_BASE_URL}/verify/{data["reference"]}", headers=headers)
    except httpx.TimeoutException as e:
        raise HTTPException(status_code=500, detail=str(e))
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

    if response.status_code != 200:
        raise HTTPException(status_code=response.status_code, detail=response.json())

    return {
        "statusCode": 200,
        "message": "Payment created successfully",
        "response": response.json(),
        "data": (response.json())["data"],
    }



# [ FLUTTERWAVE PAYMENT ]
FLW_SECRET_KEY = os.getenv('FLW_SECRET_KEY')
FLW_BASE_URL = 'https://api.flutterwave.com/v3'

@app.post("/payment/flutterwave", status_code=status.HTTP_200_OK, tags=["PAYMENT"])
@app.post("/payment/flutterwave/", status_code=status.HTTP_200_OK, tags=["PAYMENT"])
def create_payment_flutterwave(data: flutterwave_payment_pydantic_model):
    headers = {
        "Authorization": f"Bearer {FLW_SECRET_KEY}",
        "Content-Type": "application/json"
    }
    
    data = data.dict()
    data["tx_ref"] = "REF-{}".format(randint(100000000, 999999999))
    data["currency"] = "NGN"
    # data["currency"] = "USD"
    # data["payment_options"] = "card, account, googlepay, applepay"
    data["amount"] = str(data["amount"])

    amount_format = ""

    if "," in data["amount"]:
        amount_format = (data["amount"]).replace(",","")
    elif (data["amount"]).endswith(".00"):
        amount_format = data["amount"][:-3]

    if amount_format.endswith(".00"):
        amount_format = amount_format[:-3]
    elif "," in amount_format:
        amount_format = (amount_format).replace(",","")

    if len(amount_format) <= 0:
        amount_format = data["amount"]
    
    # flutterwave payment payload
    payload = {
        "tx_ref": data["tx_ref"],
        # "amount": int(amount_format) * per_dollar,
        "amount": int(amount_format),
        "currency": data["currency"],
        "redirect_url": data["redirect_url"],
        # "payment_options": data["payment_options"],
        "customer": {
            "email": data["email"],
            "name": "{} {}".format(data["first_name"], data["last_name"])
        },
        "customizations": {
            "title": "Test Inc.",
            "logo": "https://luravpn.nyc3.digitaloceanspaces.com/country_icon/.misc/1731.png"
        }
    }


    try:
        with httpx.Client(timeout=Timeout(50.0)) as client:
            # set timeout to 30 seconds
            response = client.post(f"{FLW_BASE_URL}/payments", json=payload, headers=headers)
    except httpx.TimeoutException as e:
        raise HTTPException(status_code=500, detail=str(e))
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

    if response.status_code != 200:
        raise HTTPException(status_code=response.status_code, detail=response.json())
        
    # return PaymentResponse(status="success", message="Payment created successfully", data=response.json())
    return {
        "statusCode": 200,
        "message": "Payment created successfully",
        "data": (response.json())["data"]
    }
