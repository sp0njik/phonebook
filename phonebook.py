import json
import math

from prettytable import PrettyTable


class PhoneBook:
    ''' The Phonebook class is a class in which the following methods will be implemented
    - method for displaying all entries from the directory;
    - method of adding a new entry to the directory;
    - a method that allows you to edit a record;
    - method for searching for an entry in the directory
    '''

    def __init__(self, path: str):
        self.path = path
        self.__data: list[dict] = []
        try:
            f = open(self.path, 'r')
            data = f.read()
            f.close()
            self.__data = json.loads(data)
        except FileNotFoundError:
            pass

    def add_entry(self, last_name: str, first_name: str, patronymic: str, company: str, work_phone: int,
                  personal_phone: int):
        entry = {'last_name': last_name, 'first_name': first_name, 'patronymic': patronymic, 'company': company,
                 'work_phone': work_phone, 'personal_phone': personal_phone}
        self.__data.append(entry)

    def show_entries(self, page_number: int) -> list[list]:
        if 1 > page_number > math.ceil(len(self.__data) / 5):
            raise ValueError('Please enter a valid page number')
        page_entries = []
        start_entry_num = (page_number - 1) * 5
        for index, entry in enumerate(self.__data[start_entry_num:start_entry_num + 5]):
            data = list(map(str, entry.values()))
            data.insert(0, index + 1 + start_entry_num)
            page_entries.append(data)
        return page_entries

    def search_entry(self, param: str) -> list[list]:
        found_entries = []
        for index, entry in enumerate(self.__data):
            if param in list(entry.values()):
                data = list(map(str, entry.values()))
                data.insert(0, str(index + 1))
                found_entries.append(data)
        return found_entries

    def as_pretty_table(self, data_list: list[list]) -> PrettyTable:
        table = PrettyTable()
        table.field_names = ['№', 'last_name', 'first_name', 'patronymic', 'company', 'work_phone',
                             'personal_phone']
        for data in data_list:
            table.add_row(data)
        return table

    def edit_entry(self, entry_num: int, new_entry_values: dict):
        if not (1 <= entry_num <= len(self.__data)):
            raise ValueError('wrong entry number')

        updating_entry: dict = self.__data[entry_num - 1]
        updating_entry.update(new_entry_values)

    def get_entry_by_num(self, entry_num: int) -> dict:
        if not (1 <= entry_num <= len(self.__data)):
            raise ValueError('wrong entry number')

        return self.__data[entry_num - 1]

    def close(self):
        f = open('phonebook.json', 'w', encoding='utf8')
        f.write(json.dumps(self.__data))
        f.close()
