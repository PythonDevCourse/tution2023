#!/usr/bin/env python3
"""
Примеры для filter, map и reduce
"""


def test_funct(a):
    if len(a) > 5:
        return True
    else:
        return False


fruits = ["Яблоко", "Банан", "Груша", "Абрикос", "Апельсин"]
new_list = []

for fruit in fruits:
    if len(fruit) > 5:
        new_list.append(fruit)

second_new_list = filter(test_funct, fruits)

third_new_list = filter(lambda a: len(a) > 5, fruits)


print(new_list)
print(list(second_new_list))
print(list(third_new_list))

result = map(test_funct, fruits)
result_2 = map(lambda a: len(a), fruits)

print(fruits)
print(list(result))
print(list(result_2))
print(fruits)
