"""Generate sample member records for local demo and testing."""

import argparse
import calendar
import json
from datetime import date
from pathlib import Path


def build_member(
    first_name: str,
    last_name: str,
    house_num: str,
    paid_months: set[str],
    amount: int = 1000,
) -> dict:
    """Build one member record with selected months marked as paid."""
    today = date.today().isoformat()
    payment_status = {}

    for month in (month for month in calendar.month_name if month):
        is_paid = month in paid_months
        payment_status[month] = {
            "status": "Paid" if is_paid else "Unpaid",
            "amount_paid": amount if is_paid else 0,
            "date_of_payment": today if is_paid else None,
        }

    return {
        "member_id": last_name[:3].lower() + house_num.lower(),
        "first_name": first_name.lower(),
        "last_name": last_name.lower(),
        "house_num": house_num.lower(),
        "date_of_reg": today,
        "payment_status": payment_status,
    }


def build_demo_members() -> list[dict]:
    """Return demo members covering paid, unpaid, and partially paid cases."""
    months = [month for month in calendar.month_name if month]
    return [
        build_member("Ada", "Eze", "house-12a", {"January", "February", "March"}),
        build_member(
            "Bola",
            "Ike",
            "house-24b",
            {"January", "February", "March", "April", "May", "June"},
        ),
        build_member("Chidi", "Okafor", "house-36c", set(months)),
        build_member("Dami", "Adebayo", "house-48d", set()),
        build_member("Efe", "Williams", "house-50e", {"January", "March", "May"}),
    ]


def populate_file(filepath: Path) -> None:
    """Write demo member records to ``filepath`` as formatted JSON."""
    filepath.write_text(json.dumps(build_demo_members(), indent=4) + "\n")


def main() -> None:
    """Generate demo data, optionally writing to a custom output file."""
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--output",
        type=Path,
        default=Path("members.txt"),
        help="file to populate (default: members.txt)",
    )
    args = parser.parse_args()

    populate_file(args.output)
    print(f"Generated {args.output}")


if __name__ == "__main__":
    main()
