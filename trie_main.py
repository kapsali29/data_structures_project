from Trie import TrieNode
from book_handler import load_books

file = "test_dataset.csv"


def trie_search_id(req_title):
    book_list = load_books(file)
    titles = []
    for i in range(len(book_list)):
        if i == 0:
            continue
        else:
            book = book_list[i]
            title = "".join(book[2:len(book) - 2])
            titles.append(title)
    root = TrieNode()
    root.insert_many(titles)
    return root.find(req_title)


def trie_search_surname(surname):
    book_list = load_books(file)
    book_list = book_list[1:]
    surnames = []
    for book in book_list:
        author = book[3]
        author_last_name = author.split(" ")[-1]
        surnames.append(author_last_name)
    root = TrieNode()
    root.insert_many(surnames)
    return root.find(req_title)


def trie_menu():
    print("Please choose from 1-2")
    print("1. Search by inserting id: ")
    print("2. Search by inserting author's surname: ")
    user_choice = input()
    return int(user_choice)


choice = trie_menu()
if choice == 1:
    req_title = input("Please insert title to be searched: ")
    print(trie_search_id(req_title))
else:
    req_last_name = input("Please insert Author's surname to be searched: ")
    print(trie_search_surname(req_last_name))
