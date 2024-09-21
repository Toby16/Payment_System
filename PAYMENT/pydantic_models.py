from typing import Optional
from pydantic import BaseModel, EmailStr, Field


# PAYSTACK PAYMENT
class verify_paystack_payment_model(BaseModel):
    reference: str = Field(examples=["fukykuydjs"])

class paystack_model(BaseModel):
    email: str = Field(examples=["test@example.com"])
    amount: str = Field(examples=["5000"])
    currency: str = Field(examples=["NGN"])
    redirect_url: str = Field(examples=["https://google.com/"])


# FLUTTERWAVE PAYMENT
class flutterwave_weekly_model(BaseModel):
    email: str = Field(examples=["test@example.com"])
    amount: str = Field(examples=["1500"])
    currency: str = Field(examples=["NGN"])
    redirect_url: str = Field(examples=["https://google.com/"])
    first_name: str = Field(examples=["test_firstname"])
    last_name: str = Field(examples=["test_lastname"])

class flutterwave_monthly_model(BaseModel):
    email: str = Field(examples=["test@example.com"]) 
    amount: str = Field(examples=["4900"])
    currency: str = Field(examples=["NGN"])
    redirect_url: str = Field(examples=["https://google.com/"])
    first_name: str = Field(examples=["test_firstname"])
    last_name: str = Field(examples=["test_lastname"])

class flutterwave_biannual_model(BaseModel):
    email: str = Field(examples=["test@example.com"])
    amount: str = Field(examples=["24900"])
    currency: str = Field(examples=["NGN"])
    redirect_url: str = Field(examples=["https://google.com/"])
    first_name: str = Field(examples=["test_firstname"])
    last_name: str = Field(examples=["test_lastname"])

class flutterwave_yearly_model(BaseModel):
    email: str = Field(examples=["test@example.com"])
    amount: str = Field(examples=["40000"])
    currency: str = Field(examples=["NGN"])
    redirect_url: str = Field(examples=["https://google.com/"])
    first_name: str = Field(examples=["test_firstname"])
    last_name: str = Field(examples=["test_lastname"])


