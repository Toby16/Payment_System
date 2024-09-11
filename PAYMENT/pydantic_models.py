from typing import Optional
from pydantic import BaseModel, EmailStr, Field


# PAYSTACK PAYMENT
class verify_paystack_payment_model(BaseModel):
    reference: str = Field(examples=["fukykuydjs"])

class paystack_model(BaseModel):
    email: str = Field(examples=["test@example.com"])
    redirect_url: str = Field(examples=["https://localhost.com/"])


# FLUTTERWAVE PAYMENT
class flutterwave_model(BaseModel):
    email: str = Field(examples=["test@example.com"]) 
    amount: str = Field(examples=["5000"])
    currency: str = Field(examples=["NGN"])
    redirect_url: str = Field(examples=["https://localhost.com/"])
    first_name: str = Field(examples=["test_firstname"])
    last_name: str = Field(examples=["test_lastname"])
