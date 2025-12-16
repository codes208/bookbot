from stats import get_sorted_word_count, get_word_count
from stats import get_character_count, sort_on
import sys

def get_book_text(filePath):

    with open(filePath) as f:
        book_string = f.read()

    return book_string

def print_analyze(word_count, filePath, sorted_chars):
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {filePath}...")
    print("----------- Word Count ----------")
    print(f"Found {word_count} total words")
    print("--------- Character Count -------")
    for char in sorted_chars:
        if not char["char"].isalpha():
            continue
        print(f'{char["char"]}: {char["num"]}')



def main():
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    filePath = sys.argv[1]
    book_string = get_book_text(filePath)
    word_count = get_word_count(book_string)
    char_count = get_character_count(book_string)
    sorted_chars = get_sorted_word_count(char_count)
    sorted_chars.sort(reverse=True, key=sort_on)
    print_analyze(word_count, filePath, sorted_chars)
    


main()
