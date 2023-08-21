import os

from phonebook import *
print(PhoneBook.__doc__)
entry = {
    1: 'Show all entries',
    2: 'Add new entry',
    3: 'Edit entry',
    4: 'Search entry',
    5: 'Exit'
}

for num, item in entry.items():
    print(f'{num}: {item}')
print()
user_input = 0
while not (user_input == 5):
    try:
        user_input = int(input('Choose the desired menu item: '))
    except ValueError:
        print('Enter a number')
    if user_input == 1:
        PhoneBook.show_entries()
    elif user_input == 2:
        person = PhoneBook(os.getcwd())
        person.add_entry(last_name=input('Enter last name: '), first_name=input('Enter first name: '),
                         patronymic=input('Enter last patronymic: '), company=input('Enter company: '),
                         work_phone=int(input('Enter work phone number: ')),
                         personal_phone=int(input('Enter personal phone number: ')))
    elif user_input == 3:
        pass
    elif user_input == 4:
        pass
