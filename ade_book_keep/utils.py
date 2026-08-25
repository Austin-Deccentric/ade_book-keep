import json
from pathlib import Path
import shutil
from datetime import datetime
from json.decoder import JSONDecodeError
from ade_book_keep.mtypes import Member


def get_date() -> str:
    """Return the current date formatted as YYYY-MM-DD."""
    return datetime.now().strftime("%Y-%m-%d")


def log_activity(activity: str, filepath: str = "log.txt") -> None:
    """Append a timestamped activity record to the application log file."""
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    with open(filepath, "a", encoding="utf-8") as file:
        _ = file.write(f"[{timestamp}] {activity}\n")


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
    except JSONDecodeError as e:
        print('The file is corrupted:', e.msg)
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


def backup_members(filepath: str = "members.txt", backup_dir: str = "backups") -> str:
    """Copy the members data file into a backups folder with a timestamped name."""
    source = Path(filepath)
    destination_dir = Path(backup_dir)
    
    try:
        destination_dir.mkdir(parents=True, exist_ok=True)

        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        backup_path = destination_dir / f"members_backup_{timestamp}.txt"

        _ = shutil.copy2(source, backup_path)
        return str(backup_path)

    except FileNotFoundError as error:
        raise RuntimeError(f"Members file not found: {source}") from error
    except PermissionError as error:
        raise RuntimeError(
            f"Permission denied while creating backup in: {destination_dir}"
        ) from error
    except OSError as error:
        raise RuntimeError(f"Backup failed: {error}") from error
