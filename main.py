## Header to see if pycharm can push pull from my github repo.

from stats import count_words, count_characters, sort_characters
import sys

def get_book_text(path_to_file) -> str:
    file_contents = ""
    with open(path_to_file) as f:
        file_contents = f.read()
    return file_contents

def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    print("============ BOOKBOT ============")
    book_path = sys.argv[1]
    print(f"Analyzing book found at {book_path}")
    book_text = get_book_text(book_path)
    num_words = count_words(book_text)
    print("----------- Word Count ----------")
    print(f'Found {num_words} total words')
    char_count = count_characters(book_text)
    print("--------- Character Count -------")
    sorted_characters = sort_characters(char_count)
    for char_item in sorted_characters:
        print(f"{char_item['char']}: {char_item['num']}")

main()