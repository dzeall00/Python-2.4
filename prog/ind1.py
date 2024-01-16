#!/usr/bin/env python3
# -*- coding: utf-8 -*-


# Составить программу, выдающую индексы заданного элемента или сообщающую, что
# такого элемента в списке нет.


import sys


if __name__ == '__main__':
    print("Введите элементы списка через пробел: ")

    lst = list(map(int, input().split()))
        # Если список пуст, завершить программу.
    if not lst:
        print("Заданный список пуст", file=sys.stderr)
        exit(1)

    target = int(input("Введите элемент для поиска его индекса: "))

    if target in lst:
        index = [i for i, x in enumerate(lst) if x == target]
        print(f"Индекс элемента {target}: {index}")
    else:
        print(f"Элемент {target} не найден в списке")