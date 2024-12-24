# Использования параметров *args/ **kwargs
# Задача "Однокоренные":
# Напишите функцию single_root_words, которая принимает одно обязательное слово в параметр root_word,
# а далее неограниченную последовательность в параметр *other_words.
# Функция должна составить новый список same_words только из тех слов списка other_words,
# которые содержат root_word или наоборот root_word содержит одно из этих слов.
# После вернуть список same_words в качестве результата своей работы.

# Для проверки
# result1 = single_root_words('rich', 'richiest', 'orichalcum', 'cheers', 'richies')
# result2 = single_root_words('Disablement', 'Able', 'Mable', 'Disable', 'Bagel')
# print(result1)
# print(result2)
# Результат:
# ['richiest', 'orichalcum', 'richies']
# ['Able', 'Disable']

# Решение

# Объявляем функцию с одним корневым словом и неограниченным списком слов через запятую
def single_root_words(root_word, *other_words):
    # Приводим корневое слово к нижнему регистру для сравнения
    root_word_lower = root_word.lower()

    # Создаем пустой список для хранения подходящих слов
    same_words = []

    # Проверяем все слова из последовательности в параметре other_words
    for word in other_words:
        # Приводим текущее проверяемое слово к нижнему регистру
        word_lower = word.lower()

        # Указываем условия для добавления слова в список однокоренных слов
        if root_word_lower in word_lower or word_lower in root_word_lower:
            same_words.append(word)

    # Выводим список на экран
    print("Список подходящих слов:", same_words)
    return same_words


# Запрашиваем корневое слово
root_word = input("Введите корневое слово: ")

# Запрашиваем текст однокоренных слов через запятую
other_words_input = input("Введите однокоренные слова через запятую: ")

# Преобразуем введённый текст в список слов для проверки их родства с корневым словом
other_words = [word.strip() for word in other_words_input.split(',')]

# Вызов функции с введёнными данными
single_root_words(root_word, *other_words)

