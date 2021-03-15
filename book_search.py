import os
import log


class Book:

    def __init__(self):
        self.__search_str = ''
        self.list_books = self.__list_books()[0]
        self.address = self.__list_books()[1]

    def search(self):
        self.__search_str = str(input('Enter string: '))
        return self.__find_in_book()

    def __list_books(self):
        for address, dirs, list_books in os.walk('books/'):
            return list_books, address

    def __find_in_book(self):
        form_list_books = []
        for book_name in self.list_books:
            self.open_book(book_name)
            if self.__filter_string():
                form_list_books.append(book_name)
        return form_list_books

    def open_book(self, book_name):
        with open(f'{self.address}{book_name}') as file:
            try:
                self.__copy_string = file.read()

            except UnicodeDecodeError:
                with open(f'{self.address}{book_name}', encoding='UTF-8') as file:
                    self.__copy_string = file.read()
        return self.__copy_string

    def __filter_string(self):
        self.__copy_string = self.__copy_string.split('\n')
        self.__copy_string = list(filter(lambda a: a != '', self.__copy_string))
        self.__copy_string = ' '.join(self.__copy_string)
        if self.__copy_string.lower().find(self.__search_str.lower()) == -1:
            return False
        else:
            return True


b = Book()
log = log.Logs('log.log')
try:

    log.trace(b.search())
except:
    log.trace('ERROR')
