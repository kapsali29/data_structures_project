from binary_search import binarySearch
from book_handler import load_books

file = "test_dataset.csv"


def is_sorted(lst, key=lambda x: x):
    for i, el in enumerate(lst[1:]):
        if key(el) < key(lst[i]):  # i is the index of the previous element
            return False
    return True


get_id = int(input("Please provide a book id to search: "))
book_list = load_books(file)
ids = [int(book_list[i][0]) for i in range(len(book_list)) if i != 0]
if is_sorted(ids):
    if binarySearch(ids, get_id):
        print(",".join(book_list[get_id + 1]))
