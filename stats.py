def get_num_words(text):
    count = 0
    words = text.split()
    for word in words:
        count += 1
    return count

def count_characters(text):
    chars_dict = {}
    for char in text:
        char = char.lower()
        if char in chars_dict:
            chars_dict[char] +=1
        else:
            chars_dict[char] = 1
    return chars_dict

def sort_chars(char_count):
    chars_list = []
    for char, count in char_count.items():
        chars_list.append({"char": char, "count": count})
    def sort_on(dict_item):
        return dict_item["count"]
    chars_list.sort(reverse=True, key=sort_on)
    return chars_list