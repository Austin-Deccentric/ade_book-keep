from ade_book_keep.register_members import create_member
from ade_book_keep.utils import add_member, load_members


first_name = input("Enter first name: ")
last_name = input("Enter last name: ")
house_num = input("Enter house number: ")

new_member = create_member(first_name, last_name, house_num)
add_member(new_member)
members = load_members()

for member in members:
    print(member['first_name'])
    print(member['last_name'])
    print(member['house_num'])
    print(member['date_of_reg'])
    print(member['id'])