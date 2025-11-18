import sys
from stats import (
    get_num_words,
    get_char_list,
)

def main():
    if not len(sys.argv) == 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    book_path = sys.argv[1]
    text_of_book = get_book_text(book_path)
    num_words = get_num_words(text_of_book)
    chars_list = get_char_list(text_of_book)
    print("============ BOOKBOT ============")
    print("Analyzing book found at books/frankenstein.txt...")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")
    for index in chars_list:
        if index["char"].isalpha():
            print(f"{index["char"]}: {index["num"]}")
    print("============= END ===============")

    
def get_book_text(filepath):
    with open(filepath) as file:
        return file.read()

main()