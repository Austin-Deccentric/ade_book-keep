import json
from ade_book_keep.mtypes import Member


def save_members(members: list[Member], filepath: str = "members.txt") -> None:
    with open(filepath, "w") as f:
        json.dump(members, f, indent=4)

def load_members(filepath: str = "members.txt") -> list[Member]:
    try:
        with open(filepath, "r") as f:
            return json.load(f)
    except FileNotFoundError:
        return []

members = load_members()


def add_member(member: Member, filepath: str = "members.txt") -> None:
    members.append(member)
    save_members(members, filepath)
