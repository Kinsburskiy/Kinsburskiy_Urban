# Домашняя работа по уроку "Модули и пакеты"

# В модуле fake_math создать функцию divide, принимающую два параметра first и second.
# Функция должна возвращать результат деления first на second,
# но когда в second записан 0 - возвращать строку 'Ошибка'.

def divide(first, second):
    # Создаём исключение для делителя равного 0
    if second == 0:
        return "Ошибка"  # Возвращаем строку 'Ошибка', если second равно 0
    return first / second  # Возвращаем результат деления first на second

# Проверяем и выводим на экран результаты вызовов функций
# dividend = float(input("Введите число, которое делим: ",))
# divisor = float(input("Введите число, на которое делим: ",))
# first = dividend
# second = divisor
#
# result = divide(dividend, divisor)
# print(result)