import json


def load_books_from_json():
    """
    загрузка данных из файла
    """
    with open("books.json", 'r', encoding='utf-8') as file:
        books = json.load(file)
    return books


def save_books_to_json(books):
    """
    сохранение данных в файл
    """
    with open("books.json", 'w', encoding='utf-8') as file:
        json.dump(books, file, ensure_ascii=False)


def get_books():
    """
    получение всех книжек
    """
    books = load_books_from_json()
    return books


def get_books_by_id(books_id):
    """
    получение одной книги по ИД
    """
    books = load_books_from_json()
    for book in books:
        if book['id'] == books_id:
            return book


def add_book(book_data):
    """
    записывает новую книгу в файл
    :param book_data: словарь с данными книги
    """
    books = load_books_from_json()
    last_book = books[-1]
    last_id = last_book['id']
    book_data['id'] = last_id + 1
    books.append(book_data)
    save_books_to_json(books)
    return book_data


def update_book(book_id, book_data):
    """
    обновляет книгу с заданным book_id
    """
    books = load_books_from_json()
    for book in books:
        if book['id'] == book_id:
            book = book_data
            break
    save_books_to_json()


def delete_book(book_id):
    """
    удаляет книгу с указанным ИД
    """
    books = load_books_from_json()
    for index, book in enumerate(books):
        if book['id'] == book_id:
            del books[index]
            break
    save_books_to_json()
