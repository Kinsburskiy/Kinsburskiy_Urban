# Домашняя работа по уроку "Модули и пакеты"

# Импортировать в модуль module_4_1 функции divide из модулей fake_math и true_math,
# назвав их разными именами при помощи оператора as

from fake_math import divide as fake_divide
from true_math import divide as true_divide

# Вводим значения параметров функции divide из модуля fake_math
dividend_1 = float(input("1-е число, которое делим: ",)) # Проверочное число 69
divisor_1 = float(input("1-е число-делитель: ",)) # Проверочное число 3)
dividend_2 = float(input("2-е число, которое делим: ",)) # Проверочное число 3
divisor_2 = float(input("2-е число-делитель: ",)) # Проверочное число 0

# Запрашиваем значения параметров функции divide из модуля true_math
dividend_3 = float(input("3-е число, которое делим: ",)) # Проверочное число: 49
divisor_3 = float(input("3-е число-делитель: ",)) # Проверочное число: 7
dividend_4 = float(input("4-е число, которое делим: ",)) # Проверочное число: 15
divisor_4 = float(input("4-е число-делитель: ",)) # Проверочное число: 0

# Запускаем функцию divide из модуля fake_math
result1 = fake_divide(dividend_1, divisor_1)
result2 = fake_divide(dividend_2, divisor_2)

# Запускаем функцию divide из модуля true_math
result3 = true_divide(dividend_3, divisor_3)
result4 = true_divide(dividend_4, divisor_4)

# Выводим результаты
print(result1) # Требуемый результат: 23.0
print(result2) # Требуемый результат: Ошибка
print(result3) # Требуемый результат: 7.0
print(result4) # Требуемый результат: inf
