import json
from ade_book_keep.mtypes import Member


def save_members(members: list[Member], filepath: str = "members.txt") -> None:
    """Write the supplied member records to a JSON file."""
    with open(filepath, "w") as f:
        json.dump(members, f, indent=4)

def load_members(filepath: str = "members.txt") -> list[Member]:
    """Load member records from a JSON file, or return an empty list if absent."""
    try:
        with open(filepath, "r") as f:
            return json.load(f)
    except FileNotFoundError:
        return []

members = load_members()


def add_member(member: Member, filepath: str = "members.txt") -> None:
    """Append a member record to the collection and save the updated records."""
    members.append(member)
    save_members(members, filepath)


def find_member(id: str) -> Member | None:
    """Find and return a member by ID, or return ``None`` if not found."""
    for member in members:
        if member.get("member_id") == id:
            return member
    return None

    
def create_id(last_name:str, house_num:str) -> str:
    """Build a member ID from the first three letters of a surname and house number."""
    return last_name[:3] + str(house_num)


def get_months_up_to(end_month: str) -> list[str]:
    """Return a list of months up to the specified month, inclusive."""
    all_months = [
        "January", "February", "March", "April", "May", "June",
        "July", "August", "September", "October", "November", "December"
    ]
    
    end_month = end_month.capitalize()
    if end_month not in all_months:
        raise ValueError(f"'{end_month}' is not a valid month name.")
        
    return all_months[:all_months.index(end_month) + 1]