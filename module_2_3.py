# Домашняя работа по уроку "Стиль кода часть II. Цикл While"
# Задача "Нули ничто, отрицание недопустимо!"

# Исходные данные:
my_list = [42, 69, 322, 13, 0, 99, -5, 9, 8, 7, -6, 5]
# Для доступа и прохода по элементам списка создаём переменную index с начальным значением 0
index = 0
# Используем цикл while для выведения
while index < len(my_list):  # Ограничиваем выполнение цикла длиной списка
    if my_list[index] < 0:  # Условие: если число меньше 0, то выходим из цикла
        break   # Оператор, останавливающий цикл
    if my_list[index] > 0:  # Условие: если число больше 0, выводим его
        print(my_list[index])  # Выводим положительное число
    index += 1  # Последовательноый вывод положительных чисел, пока не встретится отрицательное
