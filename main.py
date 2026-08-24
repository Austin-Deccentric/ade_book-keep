from ade_book_keep.register_members import collect_dues, create_member
from ade_book_keep.utils import members
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
            "6. Exit"
        )
        action = input("Choose an option: ").strip()

        try:
            if action == "1":
                first_name = input("Enter first name: ").strip()
                last_name = input("Enter last name: ").strip()
                house_num = input("Enter house number: ").strip()
                member = create_member(first_name, last_name, house_num)
                print(f"Registered {member['first_name']} {member['last_name']}.")
            elif action == "2":
                last_name = input("Enter last name: ").strip()
                house_num = input("Enter house number: ").strip()
                amount = int(input("Enter amount paid: ").strip())
                month = input("Enter month: ").strip()
                collect_dues(last_name, house_num, amount, month)
                print("Dues recorded.")
            elif action == "3":
                end_month = input("View unpaid dues through which month? ").strip()
                print(view_unpaid_dues(members, end_month))
            elif action == "4":
                end_month = input("View paid-up members through which month? ").strip()
                print(view_up_to_date(members, end_month))
            elif action == "5":
                last_name = input("Enter last name: ").strip()
                house_num = input("Enter house number: ").strip()
                end_month = input("View history through which month? ").strip()
                print(view_member_payment_history(last_name, house_num, end_month))
            elif action == "6" or action.lower() == "exit":
                print("Goodbye!")
                return
            else:
                print("Invalid option. Please choose 1-6.")
        except (ValueError, KeyError) as error:
            print(f"Error: {error}")


if __name__ == "__main__":
    main()
