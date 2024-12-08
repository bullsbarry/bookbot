def get_num_words(text):
    return len(text.split())

def get_char_counts(text):
    chars = {}
    for char in text.lower():
        if(char in chars):
            chars[char] += 1
        else:
            chars[char] = 1
    return chars

def char_sort(dict):
    return dict["count"]

def get_char_count_list(text):
    char_counts = []
    for key, value in get_char_counts(text).items():
        if key.isalpha():
            char_counts.append({"char": key, "count": value})
    char_counts.sort(reverse = True, key=char_sort)
    return char_counts


def get_book_text(path):
    with open(path) as f:
        return f.read()

def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    num_words = get_num_words(text)
    print(f"{num_words} words found in the document")
    for char in get_char_count_list(text):
        print(f"The '{char["char"]}' character was found {char["count"]} times")

main()