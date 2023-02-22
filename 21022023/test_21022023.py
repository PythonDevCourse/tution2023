#!/usr/bin/env python3

class LinkedListItem:
    """Docstring"""
    def __init__(self, value, next_item):
        self.value = value
        self.next_item = next_item

    def link(self, next_item):
        self.next_item = next_item

    def __gt__(self, other) -> bool:
        if self.value > other.value:
            return True
        return False

    def __str__(self):
        return f"{self.value}:{self.next_item is None}"


def print_list(head: LinkedListItem) -> str:
    if head is None:
        return ""

    cur_item = head
    list_string = f"[{cur_item.value}] -> "

    while cur_item.next_item != None:
        cur_item = cur_item.next_item
        list_string += f"[{cur_item.value}] -> "

    list_string += "None"

    return list_string


def make_sort_iteration(head: LinkedListItem) -> LinkedListItem:
    cur_item = head
    shift_count = 0

    while (cur_item.next_item is not None):
        if cur_item > cur_item.next_item:
            shift_count += 1
            cur_item.value, cur_item.next_item.value = cur_item.next_item.value, cur_item.value

        cur_item = cur_item.next_item

    return (head, shift_count)


def bubble_sort(head: LinkedListItem) -> LinkedListItem:
    """
    Функция для реализация алгоритма "пузырьковой" сортировки, которая
    выражается в следующем:

    1) Берем элемент
    2) Сравниваем элемент со следующим (если он None).
    3) Если результат сравнения является "предыдущее больше, чем текущее", то
    меряем элементы местами.
    4) Доходим до конца списка считая перестановки.
    5) Повторяем п 1-4 пока количество перестаново не будет равняться нулю
    """

    shift_count = None

    while (shift_count is None or shift_count > 0):
        head, shift_count = make_sort_iteration(head)

    return head

item = LinkedListItem(34,
                      LinkedListItem(31,
                                     LinkedListItem(12,
                                                    LinkedListItem(100,
                                                                   None)
                                                    )
                                     )
                      )

print(print_list(bubble_sort(item)))
