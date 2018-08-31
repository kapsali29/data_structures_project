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


def display_book_by_title(book_list, title):
    """
    Using that function you are able to search for a book based on its title.

    :param book_list: list of books
    :param title: book title
    :return: book info
    """
    returned_data = ""
    book_list = book_list[1:]
    for book in book_list:
        if book[2] == title:
            returned_data = ",".join(book)
            break
    if returned_data == "":
        return "The requested title is not in the book list"
    else:
        return returned_data


def find_surname(book_list, author_surname):
    """
    Using that function the book search is based on author's surname.

    :param book_list: list of books
    :param author_surname: author's last name
    :return: book info
    """
    returned_data = []
    book_list = book_list[1:]
    for book in book_list:
        author = book[3]
        author_last_name = author.split(" ")[-1]
        if author_last_name == author_surname:
            returned_data.append(",".join(book))
    return returned_data


def add_book(file, ISBN, title, author, pub_year):
    """
    Using that function the user is able to add a new book

    :param file: books dataset
    :param ISBN: ISBN
    :param title: book title
    :param author: book author
    :pub_year: publication year
    :return:
    """
    book_list = load_books(file)
    last_id = int(book_list[-1][0])
    with open(file, 'a') as f:
        new_line = [str(last_id + 1), ISBN, title, author, pub_year]
        f.write(",".join(new_line))
    pass


def exit():
    """
    Using that function you exit from the program
    """
    print("Exit\n")


def menu():
    """
    That function is used to display all the 9 options.

    :return: user choice
    """
    print("Please choose from 1-9")
    print("1. Load books from file")
    print("2. Save books to file")
    print("3. Add a book")
    print("4. Delete a book by id")
    print("5. Display a book by id")
    print("6. Display a book by title")
    print("7. Display books")
    print("8. Display books by surname search")
    print("9. Exit")
    user_choice = input()
    return int(user_choice)


book_list = load_books("test_dataset.csv")
print(add_book("test_dataset.csv", '0xxxxxx', "A fouls dream", "PK Kapsalis", "2018"))
