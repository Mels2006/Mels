# 8. Dictionaries Exercise:
# Create a dictionary of book titles and their authors. Write a function to search for a book
# by its title and return the author's name.
def find_author_by_title(books, title):
    if title in books:
        return books[title]
    
books_dict = {
    "The Great Gatsby": "F. Scott Fitzgerald",
    "To Kill a Mockingbird": "Harper Lee",
    "1984": "George Orwell",
}


title_to_search = "The Great Gatsby"
author_found = find_author_by_title(books_dict, title_to_search)


if author_found:
    print(f"The author of '{title_to_search}' is {author_found}.")

