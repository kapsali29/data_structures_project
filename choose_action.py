from book_handler import menu, diplay_books, choose_exit, save_books_to_file, display_book_by_id, load_books, \
    display_book_by_title, find_surname, add_book

choice = menu()
file = "test_dataset.csv"

if choice == 7:
    diplay_books(file)
elif choice == 9:
    choose_exit()
elif choice == 2:
    new_file = input("Please write the file to store the dataset: ")
    save_books_to_file(file, new_file)
elif choice == 5:
    req_id = int(input("Please write the book id you want to search: "))
    book_list = load_books(file)
    print(display_book_by_id(book_list, req_id))
elif choice == 6:
    req_title = input("Please write the book title you want to search: ")
    book_list = load_books(file)
    print(display_book_by_title(book_list, req_title))
elif choice == 8:
    req_surname = input("Please write the author's lastname to search his books: ")
    book_list = load_books(file)
    print(find_surname(book_list, req_surname))
elif choice == 2:
    ISBN = input("Please enter ISBN: ")
    title = input("Please enter title: ")
    author = input("Please enter author: ")
    pub_year = input("Please enter publication year: ")
    add_book(file, ISBN, title, author, pub_year)
else:
    print("That option is not provided!!")
