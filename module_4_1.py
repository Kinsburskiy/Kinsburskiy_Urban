# Домашняя работа по уроку "Модули и пакеты"

# Импортировать в модуль module_4_1 функции divide из модулей fake_math и true_math,
# назвав их разными именами при помощи оператора as


from fake_math import divide as fake_divide
from true_math import divide as true_divide

# Вызываем функции
result1 = fake_divide(69, 3)
result2 = fake_divide(3, 0)
result3 = true_divide(49, 7)
result4 = true_divide(15, 0)

# Выводим результаты
print(result1)
print(result2)
print(result3)
print(result4)
