from typing import TypedDict
from enum import Enum

class PaymentStatus(Enum):
    PAID = "Paid"
    UNPAID = "Unpaid"

class MonthlyPayment(TypedDict):
    status: PaymentStatus
    amount_paid: int

class Member(TypedDict):
    id: str
    first_name: str
    last_name: str
    house_num: str
    date_of_reg: str
    payment_status: dict[str, MonthlyPayment]