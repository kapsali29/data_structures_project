import pandas as pd


def load_books(file, delimeter):
    """
    Using that function you are able to load books from a csv file
    :param file: filename
    :return:
    """
    books = pd.read_csv(file, sep=delimeter)
    return books


def add_book(*details, file):
    """
    Using that function you are able to write a new entry on data file

    :param details: book details
    :return:
    """
    books = load_books(file, delimeter=";")
    books = books.reset_index()
    books.append(list(details))
    books.to_csv(file)
    pass

