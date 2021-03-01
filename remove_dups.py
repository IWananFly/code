from collections import Counter


def remove_duplicates(x):
    res = list()
    set_x = list(set(x))
    for item in x:
        if item in set_x:
            res.append(set_x.pop(set_x.index(item)))
        if not set_x:
            break
    return res


if __name__ == '__main__':
    x = [1, 4, 7, 6, 6, 2, 8, 12, 4, 112, 323, 232, 323, 1, 1, 1, 2, 2, 2, 3, 3, 4, 7, 8, 12, 4]
    # Если порядок не важен, то просто list(set(x))
    print('set of x:\n', list(set(x)))
    # Просто в описании задачи порядок элементов остался тем же; я и подумал, что это может быть важно
    print('Using Counter keys:\n', list(Counter(x).keys()))
    # Или мой вариант
    print('x without duplicates in same order:\n', remove_duplicates(x))
