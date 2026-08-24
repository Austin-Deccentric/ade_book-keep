from ade_book_keep.utils import get_months_up_to, create_id
from ade_book_keep.mtypes import Member, UnpaidMember, PaidMember


def view_unpaid_dues(members: list[Member], end_month: str) -> list[UnpaidMember]:
    """Return each member's unpaid months from January through ``end_month``."""
    unpaid_members: list[UnpaidMember] = []
    months_up_to = get_months_up_to(end_month)
    months_unpaid: list[str] = []
    
    for member in members:
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

def view_member_payment_history(last_name: str, house_num: str, members: list[Member]) -> str:
    id  = create_id(last_name, house_num)
    for member in members:
        if member['member_id'id'] == id:
            return f'''
            Name: {member['first_name']} {member['last_name']}
            House Number: {member['house_num']}
            '''
    return ''
