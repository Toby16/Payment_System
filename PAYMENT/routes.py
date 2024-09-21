from PAYMENT import app
from fastapi import status, Depends, HTTPException, Form
from dotenv import load_dotenv

load_dotenv()

from PAYMENT.pydantic_models import (
    flutterwave_yearly_model, flutterwave_biannual_model,
    flutterwave_monthly_model, flutterwave_weekly_model,
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

@app.post("/payment/paystack/weekly", status_code=status.HTTP_200_OK, tags=["PAYSTACK PAYMENT"])
@app.post("/payment/paystack/weekly/", status_code=status.HTTP_200_OK, tags=["PAYSTACK PAYMENT"])
def create_payment_paystack(data: paystack_model):
    #return PAYSTACK_SECRET_KEY
    headers = {
        "Authorization": f"Bearer {PAYSTACK_SECRET_KEY}",
        "Content-Type": "application/json"
    }

    data = data.dict()

    # paystack payment payload
    payload = {
        "email": data["email"],
        "plan": "PLN_xu3umnqewflv26c",  # for #1,500
        "currency": data["currency"],
        "amount": str(int(data["amount"]) * 100),
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

@app.post("/payment/paystack/monthly", status_code=status.HTTP_200_OK, tags=["PAYSTACK PAYMENT"])
@app.post("/payment/paystack/monthly/", status_code=status.HTTP_200_OK, tags=["PAYSTACK PAYMENT"])
def create_payment_paystack(data: paystack_model):
    headers = {
        "Authorization": f"Bearer {PAYSTACK_SECRET_KEY}",
        "Content-Type": "application/json"
    }

    data = data.dict()

    # paystack payment payload
    payload = {
        "email": data["email"],
        "plan": "PLN_sfnh9tj4ivqn5p9",  # for #4,900
        "currency": data["currency"],
        "amount": str(int(data["amount"]) * 100),
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



@app.post("/payment/paystack/biannually", status_code=status.HTTP_200_OK, tags=["PAYSTACK PAYMENT"])
@app.post("/payment/paystack/biannually/", status_code=status.HTTP_200_OK, tags=["PAYSTACK PAYMENT"])
def create_payment_paystack(data: paystack_model):
    headers = {
        "Authorization": f"Bearer {PAYSTACK_SECRET_KEY}",
        "Content-Type": "application/json"
    }

    data = data.dict()

    # paystack payment payload
    payload = {
        "email": data["email"],
        "plan": "PLN_d03l9b8pvw0rl3x",  # for #24,900
        "currency": data["currency"],
        "amount": str(int(data["amount"]) * 100),
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



@app.post("/payment/paystack/yearly", status_code=status.HTTP_200_OK, tags=["PAYSTACK PAYMENT"])
@app.post("/payment/paystack/yearly/", status_code=status.HTTP_200_OK, tags=["PAYSTACK PAYMENT"])
def create_payment_paystack(data: paystack_model):
    headers = {
        "Authorization": f"Bearer {PAYSTACK_SECRET_KEY}",
        "Content-Type": "application/json"
    }

    data = data.dict()

    # paystack payment payload
    payload = {
        "email": data["email"],
        "plan": "PLN_kbajf1dv3v2wk7s",  # for #40,000
        "currency": data["currency"],
        "amount": str(int(data["amount"]) * 100),
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
@app.post("/payment/paystack/verify", status_code=status.HTTP_200_OK, tags=["PAYSTACK PAYMENT"])
@app.post("/payment/paystack/verify/", status_code=status.HTTP_200_OK, tags=["PAYSTACK PAYMENT"])
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
            # set timeout to 50 seconds
            response = client.get(
                "{}/verify/{}".format(PAYSTACK_BASE_URL, data["reference"]),
                headers=headers
            )
            # response = client.get(f"{PAYSTACK_BASE_URL}/verify/{data["reference"]}", headers=headers)
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

@app.post("/payment/flutterwave/weekly", status_code=status.HTTP_200_OK, tags=["FLUTTERWAVE PAYMENT"])
@app.post("/payment/flutterwave/weekly/", status_code=status.HTTP_200_OK, tags=["FLUTTERWAVE PAYMENT"])
def create_payment_flutterwave(data: flutterwave_weekly_model):
    headers = {
        "Authorization": f"Bearer {FLW_SECRET_KEY}",
        "Content-Type": "application/json"
    }
    
    data = data.dict()
    data["tx_ref"] = "REF-{}".format(randint(100000000, 999999999))
    data["currency"] = "NGN"
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
        "amount": int(amount_format),
        "currency": data["currency"],
        "redirect_url": data["redirect_url"],
        "customer": {
            "email": data["email"],
            "name": "{} {}".format(data["first_name"], data["last_name"])
        },
        "customizations": {
            "title": "Test Inc.",
            "logo": "https://luravpn.nyc3.digitaloceanspaces.com/country_icon/.misc/1731.png"
        },
        "payment_plan": "127448"  # for #1,500
    }


    try:
        with httpx.Client(timeout=Timeout(50.0)) as client:
            # set timeout to 30 seconds
            response = client.post(f"{FLW_BASE_URL}/payments", json=payload, headers=headers)
            # response = client.get(f"{FLW_BASE_URL}/payment-plans", headers=headers)
    except httpx.TimeoutException as e:
        raise HTTPException(status_code=500, detail=str(e))
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

    if response.status_code != 200:
        raise HTTPException(status_code=response.status_code, detail=response.json())
        
    return {
        "statusCode": 200,
        "message": "Payment created successfully",
        "data": (response.json())["data"]
    }


@app.post("/payment/flutterwave/monthly", status_code=status.HTTP_200_OK, tags=["FLUTTERWAVE PAYMENT"])
@app.post("/payment/flutterwave/monthly/", status_code=status.HTTP_200_OK, tags=["FLUTTERWAVE PAYMENT"])
def create_payment_flutterwave(data: flutterwave_monthly_model):
    headers = {
        "Authorization": f"Bearer {FLW_SECRET_KEY}",
        "Content-Type": "application/json"
    }
    
    data = data.dict()
    data["tx_ref"] = "REF-{}".format(randint(100000000, 999999999))
    data["currency"] = "NGN"
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
        "amount": int(amount_format),
        "currency": data["currency"],
        "redirect_url": data["redirect_url"],
        "customer": {
            "email": data["email"],
            "name": "{} {}".format(data["first_name"], data["last_name"])
        },
        "customizations": {
            "title": "Test Inc.",
            "logo": "https://luravpn.nyc3.digitaloceanspaces.com/country_icon/.misc/1731.png"
        },
        "payment_plan": "127449"  # for #4,900
    }


    try:
        with httpx.Client(timeout=Timeout(50.0)) as client:
            # set timeout to 30 seconds
            response = client.post(f"{FLW_BASE_URL}/payments", json=payload, headers=headers)
            # response = client.get(f"{FLW_BASE_URL}/payment-plans", headers=headers)
    except httpx.TimeoutException as e:
        raise HTTPException(status_code=500, detail=str(e))
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

    if response.status_code != 200:
        raise HTTPException(status_code=response.status_code, detail=response.json())
        
    return {
        "statusCode": 200,
        "message": "Payment created successfully",
        "data": (response.json())["data"]
    }


@app.post("/payment/flutterwave/biannually", status_code=status.HTTP_200_OK, tags=["FLUTTERWAVE PAYMENT"])
@app.post("/payment/flutterwave/biannually/", status_code=status.HTTP_200_OK, tags=["FLUTTERWAVE PAYMENT"])
def create_payment_flutterwave(data: flutterwave_biannual_model):
    headers = {
        "Authorization": f"Bearer {FLW_SECRET_KEY}",
        "Content-Type": "application/json"
    }

    data = data.dict()
    data["tx_ref"] = "REF-{}".format(randint(100000000, 999999999))
    data["currency"] = "NGN"
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
        "amount": int(amount_format),
        "currency": data["currency"],
        "redirect_url": data["redirect_url"],
        "customer": {
            "email": data["email"],
            "name": "{} {}".format(data["first_name"], data["last_name"])
        },
        "customizations": {
            "title": "Test Inc.",
            "logo": "https://luravpn.nyc3.digitaloceanspaces.com/country_icon/.misc/1731.png"
        },
        "payment_plan": "127450"  # for #24,900
    }


    try:
        with httpx.Client(timeout=Timeout(50.0)) as client:
            # set timeout to 30 seconds
            response = client.post(f"{FLW_BASE_URL}/payments", json=payload, headers=headers)
            # response = client.get(f"{FLW_BASE_URL}/payment-plans", headers=headers)
    except httpx.TimeoutException as e:
        raise HTTPException(status_code=500, detail=str(e))
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

    if response.status_code != 200:
        raise HTTPException(status_code=response.status_code, detail=response.json())

    return {
        "statusCode": 200,
        "message": "Payment created successfully",
        "data": (response.json())["data"]
    }

@app.post("/payment/flutterwave/yearly", status_code=status.HTTP_200_OK, tags=["FLUTTERWAVE PAYMENT"])
@app.post("/payment/flutterwave/yearly/", status_code=status.HTTP_200_OK, tags=["FLUTTERWAVE PAYMENT"])
def create_payment_flutterwave(data: flutterwave_yearly_model):
    headers = {
        "Authorization": f"Bearer {FLW_SECRET_KEY}",
        "Content-Type": "application/json"
    }
    
    data = data.dict()
    data["tx_ref"] = "REF-{}".format(randint(100000000, 999999999))
    data["currency"] = "NGN"
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
        "amount": int(amount_format),
        "currency": data["currency"],
        "redirect_url": data["redirect_url"],
        "customer": {
            "email": data["email"],
            "name": "{} {}".format(data["first_name"], data["last_name"])
        },
        "customizations": {
            "title": "Test Inc.",
            "logo": "https://luravpn.nyc3.digitaloceanspaces.com/country_icon/.misc/1731.png"
        },
        "payment_plan": "127451"  # for #40,000
    }


    try:
        with httpx.Client(timeout=Timeout(50.0)) as client:
            # set timeout to 30 seconds
            response = client.post(f"{FLW_BASE_URL}/payments", json=payload, headers=headers)
            # response = client.get(f"{FLW_BASE_URL}/payment-plans", headers=headers)
    except httpx.TimeoutException as e:
        raise HTTPException(status_code=500, detail=str(e))
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

    if response.status_code != 200:
        raise HTTPException(status_code=response.status_code, detail=response.json())
        
    return {
        "statusCode": 200,
        "message": "Payment created successfully",
        "data": (response.json())["data"]
    }
