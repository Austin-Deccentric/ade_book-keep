from typing import TypedDict


# from enum import Enum

# class PaymentStatus(Enum):
#     PAID = "Paid"
#     UNPAID = "Unpaid"

class MonthlyPayment(TypedDict):
    status: str
    amount_paid: int
    date_of_payment: str | None

class Member(TypedDict):
    member_id: str
    first_name: str
    last_name: str
    house_num: str
    date_of_reg: str
    payment_status: dict[str, MonthlyPayment]

class UnpaidMember(TypedDict):
    name: str
    months: list[str]

class PaidMember(TypedDict):
    name: str
    house_num: str
