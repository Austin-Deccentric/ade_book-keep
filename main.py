import logging

from ade_book_keep.register_members import create_member, collect_dues


first_name = input("Enter first name: ")
last_name = input("Enter last name: ")
house_num = input("Enter house number: ")

try:
    new_member = create_member(first_name, last_name, house_num)
except ValueError as e:
    logging.error(e)
    # continue

try:
    collect_dues('black','house-89', 1000, 'January' )
except ValueError as e:
    logging.error(e)
    # continue

