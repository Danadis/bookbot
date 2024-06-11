def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    num_words = get_num_words(text)
    num_char = get_char_count(text)
    print(f"{num_words} words found in the document")
    print(num_char)

def get_num_words(text):
    words = text.split()
    return len(words)

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




main()