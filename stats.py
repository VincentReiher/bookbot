def count_words(text):
    return len(text.split())

def count_characters(text):

    character_dict = {}

    for char in text:
        lowercase_char = char.lower()
        if lowercase_char in character_dict:
            character_dict[lowercase_char] += 1
        else:
            character_dict[lowercase_char] = 1

    return character_dict

def sort_on(dict):
    return dict['num']

def report_characters(character_dict):

    dict_list = []
    for key in character_dict:
        occ_dict = {
            'char': key,
            'num': character_dict[key]
        }
        dict_list.append(occ_dict)

    dict_list.sort(reverse=True, key=sort_on)

    return dict_list