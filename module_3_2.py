# Практическое задание по 3-му модулю: "Подробнее о функциях."

# Подсчёт суммы длин всех строк, не важно, являются они ключами или значениям или ещё чем-то,
# и всех чисел, не важно, являются они ключами или значениям или ещё чем-то, в коде data_structure.

# Даны параметры:
data_structure = [
    [1, 2, 3],
    {'a': 4, 'b': 5},
    (6, {'cube': 7, 'drum': 8}),
    "Hello",
    ((), [{(2, 'Urban', ('Urban2', 35))}])
]

# Определяем функцию для подсчёта параметров
def sum_lengths_and_numbers(data):
    # Создаём переменные для сложения данных суммы строк и суммы чисел
    total_length = 0
    total_sum = 0

    # Если это строка, добавляем её длину к `total_length`
    if isinstance(data, str):
        total_length += len(data)
    # Если это число (целое или дробное), добавляем его к `total_sum`
    elif isinstance(data, (int, float)):
        total_sum += data
    # Если это коллекция (список, кортеж, множество), рекурсивно обрабатываем каждую вложенную в них часть
    elif isinstance(data, (list, tuple, set)):
        for item in data:
            lengths, numbers = sum_lengths_and_numbers(item)
            total_length += lengths
            total_sum += numbers
    # Если это словарь, рекурсивно обрабатываем ключи и значения
    elif isinstance(data, dict):
        for key, value in data.items():
            lengths_key, numbers_key = sum_lengths_and_numbers(key)
            lengths_value, numbers_value = sum_lengths_and_numbers(value)
            total_length += lengths_key + lengths_value
            total_sum += numbers_key + numbers_value
    # Возвращаем сумму длин и сумму чисел
    return total_length, total_sum
# Вызываем функцию sum_lengths_and_numbers с параметрами data_structur
lengths, numbers = sum_lengths_and_numbers(data_structure)
sum_all = lengths + numbers
# Выводим результат
print("Общая сумма строк и чисел:", sum_all)


