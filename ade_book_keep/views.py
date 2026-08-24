from ade_book_keep.utils import find_member, get_months_up_to, create_id
from ade_book_keep.mtypes import Member, UnpaidMember, PaidMember


def view_unpaid_dues(members: list[Member], end_month: str) -> list[UnpaidMember]:
    """Return each member's unpaid months from January through ``end_month``."""
    unpaid_members: list[UnpaidMember] = []
    months_up_to = get_months_up_to(end_month)
    for member in members:
        months_unpaid: list[str] = []
        for month in months_up_to:
            if member['payment_status'][month]['status'] == 'Unpaid':
                months_unpaid.append(month)
        if months_unpaid:
            unpaid_members.append({
                'name': member['first_name'] + ' ' + member['last_name'],
                'months': months_unpaid,
            })
    return unpaid_members



def view_up_to_date(members: list[Member], end_month: str) -> list[PaidMember]:
    """Return members who have paid their dues for every month through ``end_month``."""
    months_up_to = get_months_up_to(end_month)
    paid_members: list[PaidMember] = []

    for member in members:
        has_paid_all_months = all(
            member["payment_status"][month]["status"] == "Paid"
            for month in months_up_to
        )

        if has_paid_all_months:
            paid_members.append({
                "name": f"{member['first_name']} {member['last_name']}",
                "house_num": member["house_num"],
            })

    return paid_members

def view_member_payment_history(last_name: str, house_num: str, end_month: str = "December") -> str:
    """Return formatted payment history for a member through ``end_month``."""
    member_id = create_id(last_name.lower(), house_num.lower())
    member = find_member(member_id)

    if not member:
        raise ValueError("Member not found")

    months_up_to = get_months_up_to(end_month)
    payment_history = []

    for month in months_up_to:
        payment = member["payment_status"][month]

        if payment["status"] == "Paid":
            payment_history.append(
                f"{month}: Paid on {payment['date_of_payment']} " + f"(Amount: {payment['amount_paid']})"
            )
        else:
            payment_history.append(f"{month}: Unpaid")

    return f"""
Name: {member['first_name']} {member['last_name']}
House Number: {member['house_num']}

Payment History:
{'\n'.join(payment_history)}
"""
