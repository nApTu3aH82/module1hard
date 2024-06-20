grades = [[5, 3, 3, 5, 4], [2, 2, 2, 3], [4, 5, 5, 2], [4, 4, 3], [5, 5, 5, 4, 5]]
students = {'Johnny', 'Bilbo', 'Steve', 'Khendrik', 'Aaron'}
students_list = sorted(list(students)) # Создаем отсортированный список студентов
average_score = {} # создаем пустой словарь

count_students = 0 # Обнуляем счетчик количества студентов
for name_students in students_list:
    grades_ = grades[count_students]
    sum = 0 # обнуляем сумму оценок
    count = 0 # обнуляем количество оценок
    for sum_ in grades_:
        sum = sum + int(sum_)
        count += 1
    average_sum = sum / count # находим средний балл студента
    average_score[name_students] = average_sum # записываем студенту его средний балл
    count_students += 1
print(average_score)
