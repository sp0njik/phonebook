class PhoneBook:
    ''' The Phonebook class is a class in which the following methods will be implemented
    - method for displaying all entries from the directory;
    - method of adding a new entry to the directory;
    - a method that allows you to edit a record;
    - method for searching for an entry in the directory
    '''

    def __init__(self, path: str):

        self.path = path
        self.__data = []

    def add_entry(self, last_name: str, first_name: str, patronymic: str, company: str, work_phone: int,
                  personal_phone: int):
        entry = {'last_name': last_name, 'first_name': first_name, 'patronymic': patronymic, 'company': company,
                 'work_phone': work_phone, 'personal_phone': personal_phone}
        f = open('phonebook.txt', 'w', encoding='utf8')
        f.write(str(self.__data.append(entry)))
        f.flush()
        f.close()

    def show_entries(self, page_number: int):
        if 1 > page_number > len(self.__data) / 5:
            raise ValueError('Please enter a valid page number')
        table_items = 'last_name', 'first_name', 'patronymic', 'company', 'work_phone', 'personal_phone'
        table = '\t|\t'.join(table_items)
        start_entry_num = (page_number - 1) * 5
        if len(self.__data) == 0:
            f = open('phonebook.txt', 'w', encoding='utf8')
            f.write(table)
            f.flush()
            f.close()
        else:
            for entry in self.__data[start_entry_num:start_entry_num + 5]:
                table += str(entry + 1) + '|' + '\t|\t'.join(self.__data[entry].values())
                f = open('phonebook.txt', 'w', encoding='utf8')
                f.write(table)
                f.flush()
                f.close()
        print('Open file phonebook.txt')
