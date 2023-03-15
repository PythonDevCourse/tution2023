"""
Docstring 2

>>> compact ([1,2,3])
'1,2,3'
"""


def compact(L):
    """
    Функция, которая должна преобразовывать список к строке совершенно
    специальным образом.

    Еще одна строка описания.

    >>> compact([1,3,5])
    '1,3,5'
    """
    if L == []:
        return ""
    elif L is None:
        return ""
    L = sorted(L)
    prev = L[0]
    out_str = str(prev)
    for i in L[1:]:
        if i - prev == 1:
            prev = i
            continue
        if i - prev != 1:
            # out_str = out_str + "-" + str(prev) + "," + str(i)
            out_str = out_str + "," + str(i)
            prev = i
    return out_str


if __name__ == "__main__":
    import doctest

    doctest.testmod()

    a = compact([1, 3, 5])
    print(a)
