import pandas as pd
import csv


def file_preprocessing(file, new_file):
    """
    Using that function the initial dataset is modified for better processing.

    :param file: dataset
    :param new_file: file where the processed data will be stored
    :return:
    """
    with open(file, encoding="utf-8", errors='ignore') as file:
        lines = file.readlines()
        with open(new_file, "w") as f:
            for line in lines:
                cleaned_data = [substring for substring in line.split("\"") if substring != ',' and substring != '']
                if cleaned_data:
                    new_line = ",".join(cleaned_data)
                    f.write(new_line)
                else:
                    continue


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


file_preprocessing("cleared_dataset.csv", "final_dataset.csv")
