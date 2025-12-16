def get_word_count(book_string):
    word_list = []
    word_list = book_string.split()
    word_count = len(word_list)

    return word_count

def get_character_count(book_string):
    character_count = {}

    for word in book_string:
        word = word.lower()
        for char in word:
            if char in character_count:
                character_count[char] += 1
            else:
                character_count[char] = 1


    return character_count

def sort_on(char_count):
    return char_count["num"]

def get_sorted_word_count(char_count):
    char_count_list = []

    for char in char_count:
        new_dict_char_count = {"char": char, "num": char_count[char]}
        char_count_list.append(new_dict_char_count)

    return char_count_list



