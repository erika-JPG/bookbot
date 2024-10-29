def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    word_count = get_word_count(text)
    character_count = count_characters(text)

    print(character_count)

def get_word_count(text):
    words = text.split()
    return words

def get_book_text(path):
    with open(path) as f:
        return f.read()

def get_word_count(text):
    words = text.split()
    return len(words)

def count_characters(text):
    lower_text = text.lower()
    character_count = {}
    for letter in lower_text:
        if letter in character_count:
            character_count[letter] += 1
        else:
            character_count[letter] = 1
    return character_count

main()