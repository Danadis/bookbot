import sys
from stats import (
        get_num_words,
    )

def main():
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    book_path = sys.argv[1]

    text = get_book_text(book_path)
    num_words = get_num_words(text)
    num_char = get_char_count(text)
    book_report = send_book_report(num_char)
    ## print(num_char)
    print(f"--- Begin report of {book_path} --- ")
    print(f"{num_words} words found in the document")
    print()

    for item in book_report:
        if not item["char"].isalpha():
            continue
        print(f"{item['char']}: {item['num']}")

    print("--- End report ---")



def get_book_text(path):
    with open(path) as f:
        return f.read()
    
def get_char_count(text):
    lowered_chars = {}

    for chars in text:
        lowered = chars.lower()
        if lowered in lowered_chars:
            lowered_chars[lowered] += 1
        else:
            lowered_chars[lowered] = 1
    return lowered_chars

def sort_char(num_char):
        return num_char["num"]

def send_book_report(num_chars_report):
    sorted_letters = []

    for char in num_chars_report:
        sorted_letters.append({"char": char, "num": num_chars_report[char]})
    sorted_letters.sort(reverse=True, key=sort_char)
    return sorted_letters




main()