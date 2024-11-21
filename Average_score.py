students = {'Johnny', 'Bilbo', 'Steve', 'Khendrik', 'Aaron'}  # имена всех учеников в классе
grades = [[5, 3, 3, 5, 4], [2, 2, 2, 3], [4, 5, 5, 2], [4, 4, 3], [5, 5, 5, 4, 5]]  # оценки учеников в алфавитном порядке
grades_1 = grades[0] # оценки ученика 1
grades_2 = grades[1] # оценки ученика 2
grades_3 = grades[2] # оценки ученика 3
grades_4 = grades[3] # оценки ученика 4
grades_5 = grades[4] # оценки ученика 5
total_1 = sum(grades_1) # сумма оценок ученика 1
total_2 = sum(grades_2) # сумма оценок ученика 2
total_3 = sum(grades_3) # сумма оценок ученика 3
total_4 = sum(grades_4) # сумма оценок ученика 4
total_5 = sum(grades_5) # сумма оценок ученика 5
number_1 = len(grades_1) # количество оценок ученика 1
number_2 = len(grades_2) # количество оценок ученика 2
number_3 = len(grades_3) # количество оценок ученика 3
number_4 = len(grades_4) # количество оценок ученика 4
number_5 = len(grades_5) # количество оценок ученика 5
average_1 = float((total_1) / (number_1)) # средняя оценка ученика 1
average_2 = float((total_2) / (number_2)) # средняя оценка ученика 2
average_3 = float((total_3) / (number_3)) # средняя оценка ученика 3
average_4 = float((total_4) / (number_4)) # средняя оценка ученика 4
average_5 = float((total_5) / (number_1)) # средняя оценка ученика 5
alphabetical = sorted(students) # список имен учеников в алфавитном порядке
Average_score = ({alphabetical[0]: average_1, alphabetical[1]: average_2, alphabetical[2]:
    average_3, alphabetical[3]: average_4, alphabetical[4]: average_5}) # средние оценки списка учеников в алфавитном порядке
print(Average_score)

