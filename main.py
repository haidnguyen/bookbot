def main():
    text = get_book_text("books/frankenstein.txt")
    word_count = get_num_words(text)
    char_dict = char_count(text)
    print("--- Begin report of books/frankenstein.txt")
    print(f"{word_count} words found in the document\n")

    for record in convert_to_sorted_list(char_dict):
        print(f"The '{record["char"]}' character was found {record["count"]} times")
    print("--- End report ---")

def sort_on(dict):
    return dict["count"]

def get_book_text(path):
    with open(path) as f:
        return f.read()
    
def get_num_words(text):
    words = text.split()
    return len(words)

def char_count(text):
    result_dict = {}
    for char in text:
        lowercase_char = char.lower()
        if lowercase_char in result_dict:
            result_dict[lowercase_char] += 1 
        else:
            result_dict[lowercase_char] = 1
    return result_dict

def convert_to_sorted_list(dict):
    records = []
    for char in dict:
        if char.isalpha():
            records.append({"char": char, "count": dict[char]})
            records.sort(reverse=True, key=sort_on)
    return records

main()
