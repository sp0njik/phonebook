import os

from phonebook import *

entry: dict = {
    1: "Show all entries",
    2: "Add new entry",
    3: "Edit entry",
    4: "Search entry",
    5: "Exit",
}
for num, item in entry.items():
    print(f"{num}: {item}")
print()
phonebook: PhoneBook = PhoneBook(os.getcwd() + "/phonebook.json")
user_input: int = 0
while not (user_input == 5):
    try:
        user_input = int(input("Choose the desired menu item: "))
    except ValueError:
        print("Enter a number")
    if user_input == 1:
        page_number = 1
        result = phonebook.show_entries(page_number)
        while True:
            table = phonebook.as_pretty_table(result)
            print(table)
            page_number += 1
            result = phonebook.show_entries(page_number)
            if not result:
                break
            while True:
                next = input("next page ? [Y/N]: ").upper()
                if next not in ["Y", "N"]:
                    print("input Y or N")
                else:
                    break
            if next == "N":
                break
    elif user_input == 2:
        phonebook.add_entry(
            last_name=input("Enter last name: "),
            first_name=input("Enter first name: "),
            patronymic=input("Enter last patronymic: "),
            company=input("Enter company: "),
            work_phone=int(input("Enter work phone number: ")),
            personal_phone=int(input("Enter personal phone number: ")),
        )
    elif user_input == 3:
        entry_num = int(input("Enter the entry num: "))
        entry = phonebook.get_entry_by_num(entry_num)
        entry_values = list(entry.values())
        entry_values.insert(0, entry_num)
        table = phonebook.as_pretty_table([entry_values])
        print(table)
        print(
            "Enter a new value for the field or leave it blank so as not to change it: "
        )
        changed_entry = entry.copy()
        for k, v in changed_entry.items():
            new_value = input(f"{k} [{v}]: ")
            if new_value:
                changed_entry[k] = new_value
        phonebook.edit_entry(entry_num, changed_entry)
    elif user_input == 4:
        param = input(
            "To search, enter last name/first name/patronymic/company/work phone or personal phone: "
        )
        found_entries = phonebook.search_entry(param)
        if found_entries:
            table = phonebook.as_pretty_table(found_entries)
            print(table)
        else:
            print("Record not found")

phonebook.close()
