import calendar
from datetime import datetime
from ade_book_keep.mtypes import Member
from ade_book_keep.utils import save_members, members, add_member, create_id, find_member


def create_member(first_name: str, last_name: str, house_num: str) -> Member:
    """Create, store, and return a new member with unpaid monthly dues."""
    last_name = last_name.lower()
    house_num = house_num.lower()
    member_id = create_id(last_name, house_num)

    if find_member(member_id) is not None:
        raise ValueError("Member already exists")

    member: Member = {
        "member_id": member_id,
        "first_name": first_name.lower(),
        "last_name": last_name,
        "house_num": house_num,
        "date_of_reg": datetime.now().strftime("%Y-%m-%d"),
        "payment_status": {
            month: {"status": "Unpaid", "amount_paid": 0, "date_of_payment": None}
            for month in calendar.month_name if month
        }
    }
    add_member(member)
    return member



def collect_dues(last_name: str, house_num: str, amount: int, month: str) -> None:
    """Record a dues payment for a member identified by surname and house number."""
    member_id = create_id(last_name.lower(), house_num.lower())
    member = find_member(member_id)

    if member is None:
        raise ValueError("Member not found")

    if member["payment_status"][month]["status"] == "Paid":
        raise ValueError("Dues already paid")

    member["payment_status"][month] = {
        "status": "Paid",
        "amount_paid": amount,
        "date_of_payment": datetime.now().strftime("%Y-%m-%d"),
    }

    save_members(members)

