import json

from ade_book_keep.register_members import collect_dues, create_member
from ade_book_keep.utils import members, log_activity, backup_members
from ade_book_keep.views import (
    view_member_payment_history,
    view_unpaid_dues,
    view_up_to_date,
)


def main() -> None:
    """Run the interactive estate records application."""
    print("Welcome to Ade's Estate Records!")

    while True:
        print(
            "\n1. Register member\n"
            "2. Collect dues\n"
            "3. View unpaid dues\n"
            "4. View up-to-date members\n"
            "5. View member payment history\n"
            "6. Backup member records\n"
            "7. Exit"
        )
        action = input("Choose an option: ").strip()

        try:
            if action == "1":
                first_name = input("Enter first name: ").strip()
                last_name = input("Enter last name: ").strip()
                house_num = input("Enter house number: ").strip()
                member = create_member(first_name, last_name, house_num)
                print(f"Registered {member['first_name'].title()} {member['last_name'].title()}.")
                log_activity(
                        f"Registered member: {member['first_name'].title()} "
                        f"{member['last_name'].title()} (House {member['house_num']})"
                    )
                
            elif action == "2":
                last_name = input("Enter last name: ").strip()
                house_num = input("Enter house number: ").strip()
                amount = int(input("Enter amount paid: ").strip())
                month = input("Enter month (eg: January): ").strip()
                collect_dues(last_name, house_num, amount, month)
                print("Dues recorded.")
                log_activity(
                    f"Recorded payment: {last_name.title()} (House {house_num}), "
                    f"{month}, amount {amount}"
                )
                
            elif action == "3":
                end_month = input("View unpaid dues through which month? ").strip()
                unpaid_members = view_unpaid_dues(members, end_month)
                for _member in unpaid_members:
                    print(f'{_member["name"].title()} - {", ".join(_member["months"])}')
                log_activity(f"Viewed unpaid-dues report through {end_month}")
                
            elif action == "4":
                end_month = input("View paid-up members through which month? ").strip()
                up_to_date_members = view_up_to_date(members, end_month)
                for _member in up_to_date_members:
                    print(f'{_member["name"].title()} - {_member["house_num"]}')
                log_activity(f"Viewed paid-up-members report through {end_month}")
                
            elif action == "5":
                last_name = input("Enter last name: ").strip()
                house_num = input("Enter house number: ").strip()
                end_month = input("View history through which month? ").strip()
                print(view_member_payment_history(last_name, house_num, end_month))
                log_activity(
                    f"Viewed payment history: {last_name.title()} "
                    f"(House {house_num}) through {end_month}"
                )
                
            elif action == "6":
                backup_path = backup_members()
                print(f"Backup saved to {backup_path}")
                log_activity(f"Backed up member records to {backup_path}")
            
            elif action == "7" or action.lower() == "exit":
                log_activity("Application closed by user")
                print("Goodbye!")
                return
            else:
                print("Invalid option. Please choose 1-7.")
    
        except json.JSONDecodeError as error:
            log_activity(f"Data file corrupted during menu action {action}: {error}")
            print(f"Error: members.txt appears corrupted ({error.msg}).")
        except (ValueError, KeyError) as error:
            log_activity(f"Error during menu action {action}: {error}")
            print(f"Error: {error}")
        except FileNotFoundError as error:
            log_activity(f"Missing file during menu action {action}: {error}")
            print(f"Error: required file not found ({error.filename}).")
        except OSError as error:
            log_activity(f"File I/O error during menu action {action}: {error}")
            print(f"Error: could not read/write a file ({error}).")
        except Exception as error:
            log_activity(f"Unexpected error during menu action {action}: {error!r}")
            print(f"Unexpected error: {error}")


if __name__ == "__main__":
    main()
