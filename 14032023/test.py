"""
Docstring 2

>>> compact ([1,2,3])
'1-3'
"""


def compact(L):
    """
    Функция, которая должна преобразовывать список к строке совершенно
    специальным образом.

    Еще одна строка описания.

    >>> compact([1,3,5])
    '1,3,5'
    >>> compact([1,2,3,5])
    '1-3,5'
    >>> compact([1,3,5,6,10,11,12,16,17,18])
    '1-6,10-12,16-18'
    """
    if L == []:
        return ""
    elif L is None:
        return ""

    in_interval = False

    interval_start = None

    L = sorted(L)
    prev = None
    out_str = ""

    last_elem = L[-1]

    for i in L:
        if prev is None:
            out_str = f"{i}"
            prev = i
            continue
        if i - prev == 1 and not in_interval:
            interval_start = prev
            in_interval = True
            print(f"Попали в интервал {i} {prev}")
            prev = i
            continue
        if i - prev != 1 and in_interval:
            if in_interval and prev - interval_start != 1:
                out_str = out_str + f"-{prev},{i}"
            if in_interval and prev - interval_start == 1:
                out_str = out_str + f",{prev},{i}"
            in_interval = False
            interval_start = None
            continue
        if i - prev != 1 and not in_interval:
            out_str += f",{i}"
            continue
        if i == last_elem and in_interval:
            out_str += f"-{i}"
        if i == last_elem and not in_interval:
            out_str += f",{i}"
        prev = i
    return out_str


if __name__ == "__main__":
    # import doctest

    # doctest.testmod()

    a = compact([1, 2, 3, 5])
    print("==================")
    print(a)
