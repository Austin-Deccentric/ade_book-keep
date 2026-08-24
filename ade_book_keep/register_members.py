import calendar
from datetime import datetime
from ade_book_keep.mtypes import Member, PaymentStatus
from ade_book_keep.utils import add_member, members



def create_id(last_name:str, house_num:str) -> str:
    return last_name[:3] + str(house_num)

def create_member(first_name: str, last_name: str, house_num: str) -> Member:
    id = create_id(last_name, house_num)
    
    if any(member.get("id") == id for member in members):
        raise ValueError("Member already exists")
    
    member: Member = {
        "id": id,
        "first_name": first_name,
        "last_name": last_name,
        "house_num": house_num,
        "date_of_reg": datetime.now().strftime("%Y-%m-%d"),
        "payment_status": {
            month: {"status": PaymentStatus.UNPAID, "amount_paid": 0}
            for month in calendar.month_name if month
        }
    }
    add_member(member)
    return member


def collect_dues(
    last_name: str, house_num: str,
    amount: int, month: str
):
    id = create_id(last_name, house_num)
    
    for member in members:
        if member.get("id") == id:
            member["payment_status"][month] = {"status": PaymentStatus.PAID, "amount_paid": amount}
            break
    else:
        raise ValueError("Member not found")
    add_member(member)
