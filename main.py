def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    word_count = get_word_count(text)
    character_count = count_characters(text)
    report = print_report(character_count)

    print(f"--- Begin report of {book_path} ---")
    print(f"\n{word_count} words found in the document")
    print(f"{report} --- End report ---")

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

def print_report(character_count_object):

    report = ''

    def sort_on(dict):
        return dict["char"]
    
    array_of_characters = [{"char": key, "count": value} for key, value in character_count_object.items()]
    
    array_of_characters.sort(reverse=False, key=sort_on)

    for item in array_of_characters:
        if item["char"].isalpha():
            report += f"The '{item["char"]}' character was found {item["count"]} times \n"
    return report

main()