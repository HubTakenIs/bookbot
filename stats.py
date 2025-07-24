from utils import get_book_text

def word_count(file_path):
    split = get_book_text(file_path).split()
    return len(split)

def character_count(file_path):
    text = get_book_text(file_path)
    words = text.split()
    out = {}
    for word in words:
        for c in word:
            c = c.lower()
            if c in out.keys():
                out[c] +=1
            else:
                out[c] = 1
    return out

def sort_dict(dict):
    return dict['count']


def report(dict):
    out_list = []
    for key in dict:
        temp = {}
        temp['char'] = key
        temp['count'] = dict[key]
        out_list.append(temp)
    out_list.sort(reverse=True, key=sort_dict)
    return out_list
