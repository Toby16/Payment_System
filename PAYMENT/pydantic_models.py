from typing import Optional
from pydantic import BaseModel, EmailStr, Field


# PAYSTACK PAYMENT
class verify_paystack_payment_model(BaseModel):
    reference: str = Field(examples=["fukykuydjs"])

class paystack_model(BaseModel):
    amount: str = Field(examples=["4500"])
    redirect_url: str = Field(examples=["https://queens-stores.vercel.app/"])

# FLUTTERWAVE PAYMENT
class flutterwave_payment_pydantic_model(BaseModel):
    amount: str = Field(examples=["3000"])
    redirect_url: str = Field(examples=["https://queens-stores.vercel.app/"])

class flutterwave_model(BaseModel):
    amount: str = Field(examples=["450"])
