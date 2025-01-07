# Домашняя работа по уроку "Модули и пакеты"

# Создать принимающую функцию divide с двумя параметрами: first и second.
# Функция должна возвращать результат деления first на second,
# но когда в second записан 0 - возвращать бесконечность inf.
# Бесконечность импортировать из библиотеки math

# Импортируем константу бесконечности inf
from math import inf

def divide(first, second):
    # Создаём исключение для числа-делителя равного 0
    if second == 0:
        return inf  # Возвращаем константу бесконечности, если second равно 0
    return first / second  # Возвращаем функцию в виде результата деления first на second

# Проверяем и выводим на экран результаты вызовов функций
# dividend = float(input("Введите число, которое делим: ",))
# divisor = float(input("Введите число, на которое делим: ",))
# first = dividend
# second = divisor

# result = divide(dividend, divisor)
# print(result)
