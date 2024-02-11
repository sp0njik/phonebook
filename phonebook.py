import json
import math

from prettytable import PrettyTable


class PhoneBook:
    def __init__(self, path: str)-> None:
        # """
        # Инициализирует новый экземпляр класса
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
#         Добавляет новую запись в список данных.
#         Аргументы:
#         last_name (str): Фамилия человека.
#         first_name (str): Имя человека.
#         patronymic (str): Отчество человека.
#         company (str): Название компании человека.
#         work_phone (int): Рабочий телефон человека.
#         personal_phone (int): Личный телефон человека.
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
#         """
#         Показывает записи для указанного номера страницы.
#         Аргументы: page_number (int): Номер страницы, для которой нужно показать записи.
#         Возвращает: list[list]: Список списков, содержащий записи для указанной страницы.
#         """
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
#       """
#       Ищет параметр в данных и возвращает список списков, содержащих найденные записи.
#       Аргументы: param: Параметр для поиска (тип: str)
#       Возвращает: Список списков, содержащих найденные записи (тип: list[list])
#       """
        found_entries: list[list] = []
        for index, entry in enumerate(self.__data):
            if param in list(entry.values()):
                data: list = list(map(str, entry.values()))
                data.insert(0, str(index + 1))
                found_entries.append(data)
        return found_entries

    def as_pretty_table(self, data_list: list[list]) -> PrettyTable:
#         """
#         Генерирует отформатированную таблицу из данного списка данных.
#         Аргументы:  data_list (list[list]): Список списков, содержащий данные, которые будут отображены в таблице.
#         Возвращает: PrettyTable: Отформатированная таблица, сгенерированная из заданных данных.
#         """
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
#         """
#         Редактирует запись в данных с использованием предоставленного номера записи и новых значений.
#         Аргументы: entry_num (int): Номер редактируемой записи.
#                    new_entry_values (dict): Новые значения для обновления записи.
#         """
        if not (1 <= entry_num <= len(self.__data)):
            raise ValueError("wrong entry number")

        updating_entry: dict = self.__data[entry_num - 1]
        updating_entry.update(new_entry_values)

    def get_entry_by_num(self, entry_num: int) -> dict:
#         """
#         Получеает записи из __data на основе указанного номера записи.
#         Аргументы: entry_num: Целое число, представляющее номер записи для извлечения.
#         Возвращает: Словарь, представляющий данные записи.
#         """
        if not (1 <= entry_num <= len(self.__data)):
            raise ValueError("wrong entry number")

        return self.__data[entry_num - 1]

    def close(self):
#         """
#         Закрывает файл, связанный с объектом, записывает JSON-представление данных в файл, а затем закрывает его.
#         """
        f = open(self.path, "w", encoding="utf8")
        data = json.dumps(self.__data)
        f.write(data)


      
