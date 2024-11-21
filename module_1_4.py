my_string = input('В каком учебном заведении Вы учитесь программированию на Python? ')
print(my_string) # строка введённого текстового ответа
Number_of_characters = len(my_string) # количество символов введённого текста
print('Количество символов в ответе:', Number_of_characters)
print(my_string.upper()) # строка в верхнем регистре (прописные буквы)
print(my_string.lower()) # строка в нижнем регистре (строчные буквы)
print(my_string.replace(' ', '')) # строка без пробелов
print(my_string[0]) # первый символ строки
print(my_string[-1]) # последний символ строки
