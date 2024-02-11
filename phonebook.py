import json
import math

from prettytable import PrettyTable


class PhoneBook:
    def __init__(self, path: str)-> None:
        # """
        # Initializes a new instance of the class.
        # """
        self.path: str = path
        self.__data: list[dict] = []
        try:
            f = open(self.path, "r")
            data = f.read()
            f.close()
            self.__data = json.loads(data)
        except FileNotFoundError:
            pass

    def add_entry(
        self,
        last_name: str,
        first_name: str,
        patronymic: str,
        company: str,
        work_phone: int,
        personal_phone: int,
    )-> None:
        #         """
        #         Adds a new entry to the data list.
        #         Args:
        #             last_name (str): The last name of the person.
        #             first_name (str): The first name of the person.
        #             patronymic (str): The patronymic name of the person.
        #             company (str): The company name of the person.
        #             work_phone (int): The work phone number of the person.
        #             personal_phone (int): The personal phone number of the person.
        #         """
        entry = {
            "last_name": last_name,
            "first_name": first_name,
            "patronymic": patronymic,
            "company": company,
            "work_phone": work_phone,
            "personal_phone": personal_phone,
        }
        self.__data.append(entry)

    def show_entries(self, page_number: int) -> list[list]:
        if 1 > page_number > math.ceil(len(self.__data) / 5):
            raise ValueError("Please enter a valid page number")
        page_entries: list[list] = []
        start_entry_num: int = (page_number - 1) * 5
        for index, entry in enumerate(
            self.__data[start_entry_num : start_entry_num + 5]
        ):
            data = list(map(str, entry.values()))
            data.insert(0, index + 1 + start_entry_num)
            page_entries.append(data)
        return page_entries

    def search_entry(self, param: str) -> list[list]:
        found_entries: list[list] = []
        for index, entry in enumerate(self.__data):
            if param in list(entry.values()):
                data: list = list(map(str, entry.values()))
                data.insert(0, str(index + 1))
                found_entries.append(data)
        return found_entries

    def as_pretty_table(self, data_list: list[list]) -> PrettyTable:
        table: PrettyTable = PrettyTable()
        table.field_names: list = [
            "№",
            "last_name",
            "first_name",
            "patronymic",
            "company",
            "work_phone",
            "personal_phone",
        ]
        for data in data_list:
            table.add_row(data)
        return table

    def edit_entry(self, entry_num: int, new_entry_values: dict)-> None:
        """
        Edit an entry in the data list.
        Parameters:
            entry_num (int): The index of the entry to be edited.
            new_entry_values (dict): The new values to update the entry with.
        Raises:
            ValueError: If the entry number is out of range.
        """
        if not (1 <= entry_num <= len(self.__data)):
            raise ValueError("wrong entry number")

        updating_entry: dict = self.__data[entry_num - 1]
        updating_entry.update(new_entry_values)

    def get_entry_by_num(self, entry_num: int) -> dict:
        if not (1 <= entry_num <= len(self.__data)):
            raise ValueError("wrong entry number")

        return self.__data[entry_num - 1]

    def close(self):
        f = open(self.path, "w", encoding="utf8")
        data = json.dumps(self.__data)
        f.write(data)


      
