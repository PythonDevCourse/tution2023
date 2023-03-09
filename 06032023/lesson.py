#!/usr/bin/env python3


a = [5, 2, 7, 1, 9, 6, 10, 8]


def compact(input_list):
    """
    Эта функция преобразует список в нужную нам сроку
    """
    l = sorted(input_list)
    out_str = ""
    start = None
    end = None
    prev = None

    for i in l:
        if prev is None:
            prev = i
            continue
        else:
            diff = i - prev
            if diff == 1:
                start = prev
                end = i
                prev = i
            else:
                out_str += f"{start}{',' if end-start == 1 else '-'}{end},"
                prev = i
                start = None
                end = None
        if i == l[-1]:  # Последний элемент
            if start is not None and end is not None:

                out_str += f"{start}{',' if i-start == 1 else '-'}{i},"
                # ...
            else:
                out_str += f"{i}"
                # ...
    return out_str


res = compact(a)
print(res)
