import calendar
from datetime import datetime
from ade_book_keep.mtypes import Member
from ade_book_keep.utils import save_members, members, add_member



def create_id(last_name:str, house_num:str) -> str:
    """Build a member ID from the first three letters of a surname and house number."""
    return last_name[:3] + str(house_num)

def create_member(first_name: str, last_name: str, house_num: str) -> Member:
    """Create, store, and return a new member with unpaid monthly dues."""
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
            month: {"status": "Unpaid", "amount_paid": 0}
            for month in calendar.month_name if month
        }
    }
    add_member(member)
    return member


def collect_dues(
    last_name: str, house_num: str,
    amount: int, month: str
):
    """Record a dues payment for a member identified by surname and house number."""
    id = create_id(last_name, house_num)
    
    for member in members:
        if member.get("id") == id:
            if member["payment_status"][month]["status"] == "Paid":
                raise ValueError("Dues already paid")
            member["payment_status"][month] = {"status": "Paid", "amount_paid": amount}
            break
        else:
            raise ValueError("Member not found")
    save_members(members)
