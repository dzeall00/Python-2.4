#!/usr/bin/env python3
# -*- coding: utf-8 -*-


# В списке, состоящем из целых элементов, вычислить:
# 1. минимальный по модулю элемент списка;
# 2. сумму модулей элементов списка, расположенных после первого элемента, равного нулю.
# Преобразовать список таким образом, чтобы в первой его половине располагались элементы,
# стоявшие в четных позициях, а во второй половине - элементы, стоявшие в нечетных позициях.

import math
import sys


if __name__ == '__main__':
    print("Введите список целых чисел через пробел")
    input_list = list(map(int, input().split()))

    m_value = math.fabs(input_list[0])

    for i, num in enumerate(input_list):
        abs_value = math.fabs(num)
        if abs_value < m_value:
            m_value = abs_value

    summ = 0
    zero_found = False

    for num in input_list:
        if zero_found:
            summ += abs(num)
        elif num == 0:
            zero_found = True

    def rearrange_list(input_list):
        half_length = len(input_list) // 2
        rearranged_list = input_list[::2] + input_list[1::2]
        return rearranged_list

print(f"Минимального по модулю элемент списка: {int(m_value)}")
print(f"Сумма модулей элементов после первого элемента равного нулю: {summ}")
print(f"Преобразованный список: {rearrange_list(input_list)}")