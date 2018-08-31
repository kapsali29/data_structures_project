import pandas as pd
from pprint import pprint


def diplay_books(file):
    """
    Using that function you are able to load books from a csv file
    :param file: filename
    :return:
    """
    with open(file, encoding="utf-8", errors='ignore') as file:
        lines = file.readlines()
        for line in lines:
            print(line.strip('\n'))


def load_books(file):
    """
    Using that function the books dataset is loaded to a list

    :param file: books dataset
    :return: list of books
    """
    with open(file, encoding="utf-8", errors='ignore') as file:
        lines = file.readlines()
        book_list = []
        for line in lines:
            line = line.strip('\n')
            substrings = line.split(",")
            title = "".join(substrings[2:len(substrings) - 2])
            sub_list = [substrings[0], substrings[1], title, substrings[-2], substrings[-1]]
            book_list.append(sub_list)
        return book_list


def save_books_to_file(dataset, file):
    """
    Using that function you are able to store the books data to any file you want.

    :param dataset: books dataset
    :param file: file to store
    :return:
    """
    with open(dataset, encoding="utf-8", errors='ignore') as data:
        lines = data.readlines()
        with open(file, "w") as f:
            for line in lines:
                f.write(line)


def display_book_by_id(book_list, book_id):
    """
    Using that function you are able to find a book by id and print it to the console.

    :param book_list: list of books
    :param book_id: id to find
    :return:
    """
    returned_data = ""
    book_list = book_list[1:]
    for book in book_list:
        if int(book[0]) == book_id:
            returned_data = ",".join(book)
            break
    if returned_data == "":
        return "The requested ID is not in the book list"
    else:
        return returned_data


book_list = load_books("test_dataset.csv")
print(display_book_by_id(book_list, 99))
