def count_words(file_contents) -> int:
    words = file_contents.split()
    return len(words)

def count_characters(file_contents) -> dict[str, int]:
    char_count = {}
    for char in file_contents:
        char = char.lower()
        if char in char_count:
            char_count[char] += 1
        else:
            char_count[char] = 1
    return char_count

def sort_on(dict):
    return dict["num"]

def sort_characters(dict):
    sorted_list = []
    for (key, value) in dict.items():
        sorted_list.append({"char": key, "num": value})

    sorted_list.sort(reverse=True, key=sort_on)
    return sorted_list