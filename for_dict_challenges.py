# Задание 1
# Дан список учеников, нужно посчитать количество повторений каждого имени ученика
# Пример вывода:
# Вася: 1
# Маша: 2
# Петя: 2

students = [
    {'first_name': 'Вася'},
    {'first_name': 'Петя'},
    {'first_name': 'Маша'},
    {'first_name': 'Маша'},
    {'first_name': 'Петя'},
]
names_dict = {}
for student in students:
    student_name = student['first_name']
    names_dict[student_name] = names_dict.get(student_name, 0) + 1

for name in names_dict.keys():
    print(f'{name}: {names_dict[name]}')


# Задание 2
# Дан список учеников, нужно вывести самое часто повторящееся имя
# Пример вывода:
# Самое частое имя среди учеников: Маша
students = [
    {'first_name': 'Вася'},
    {'first_name': 'Петя'},
    {'first_name': 'Маша'},
    {'first_name': 'Маша'},
    {'first_name': 'Оля'},
]
names_dict = {}
for student in students:
    student_name = student['first_name']
    names_dict[student_name] = names_dict.get(student_name, 0) + 1

max_value = max(names_dict.values())
for name in names_dict:
    if names_dict[name] == max_value:
        print(f'Самое частое имя среди учеников: {name}')

# Задание 3
# Есть список учеников в нескольких классах, нужно вывести самое частое имя в каждом классе.
# Пример вывода:
# Самое частое имя в классе 1: Вася
# Самое частое имя в классе 2: Маша

school_students = [
    [  # это – первый класс
        {'first_name': 'Вася'},
        {'first_name': 'Вася'},
    ],
    [  # это – второй класс
        {'first_name': 'Маша'},
        {'first_name': 'Маша'},
        {'first_name': 'Оля'},
    ],[  # это – третий класс
        {'first_name': 'Женя'},
        {'first_name': 'Петя'},
        {'first_name': 'Женя'},
        {'first_name': 'Саша'},
    ],
]
for index, students in enumerate(school_students):
    names_dict = {}
    for student in students:
        student_name = student['first_name']
        names_dict[student_name] = names_dict.get(student_name, 0) + 1

    max_value = max(names_dict.values())
    for name in names_dict:
        if names_dict[name] == max_value:
            print(f'Самое частое имя в классе {index+1}: {name}')


# Задание 4
# Для каждого класса нужно вывести количество девочек и мальчиков в нём.
# Пример вывода:
# Класс 2a: девочки 2, мальчики 0 
# Класс 2б: девочки 0, мальчики 2

school = [
    {'class': '2a', 'students': [{'first_name': 'Маша'}, {'first_name': 'Оля'}]},
    {'class': '2б', 'students': [{'first_name': 'Олег'}, {'first_name': 'Миша'}]},
    {'class': '2б', 'students': [{'first_name': 'Даша'}, {'first_name': 'Олег'}, {'first_name': 'Маша'}]},
]
is_male = {
    'Олег': True,
    'Маша': False,
    'Оля': False,
    'Миша': True,
    'Даша': False,
}

sex_count = {}
for school_class in school:
    class_name = school_class.get('class')
    old_class_info = sex_count.get(class_name, {'male': 0, 'female': 0})
    male = old_class_info.get('male')
    female = old_class_info.get('female')
    for student in school_class.get('students'):
        if is_male.get(student['first_name']):
            male += 1
        else:
            female += 1
    sex_count[class_name] = {'male': male, 'female': female}
for classInfo in sex_count.keys():
    print(f"Класс {classInfo}: девочки {sex_count.get(classInfo).get('female')} мальчики {sex_count.get(classInfo).get('male')}")

# на 4 задании чуть мозги в трубочку не свернулись. чувствую, что можно по другому, но не знаю как


# Задание 5
# По информации о учениках разных классов нужно найти класс, в котором больше всего девочек и больше всего мальчиков
# Пример вывода:
# Больше всего мальчиков в классе 3c
# Больше всего девочек в классе 2a

school = [
    {'class': '2a', 'students': [{'first_name': 'Маша'}, {'first_name': 'Оля'}]},
    {'class': '3c', 'students': [{'first_name': 'Олег'}, {'first_name': 'Миша'}]},
]
is_male = {
    'Маша': False,
    'Оля': False,
    'Олег': True,
    'Миша': True,
}

sex_count = {}
for school_class in school:
    class_name = school_class.get('class')
    old_class_info = sex_count.get(class_name, {'male': 0, 'female': 0})
    male = old_class_info.get('male')
    female = old_class_info.get('female')
    for student in school_class.get('students'):
        if is_male.get(student['first_name']):
            male += 1
        else:
            female += 1
    sex_count[class_name] = {'male': male, 'female': female}


max_info = {'class_female': None, 'female_count': 0, 'class_male': None, 'male_count': 0}
for classInfo in sex_count.keys():
    if sex_count.get(classInfo).get('female') > max_info.get('female_count'):
        max_info['class_female'] = classInfo
        max_info['female_count'] = sex_count.get(classInfo).get('female')
    if sex_count.get(classInfo).get('male') > max_info.get('male_count'):
        max_info['class_male'] = classInfo
        max_info['male_count'] = sex_count.get(classInfo).get('male')

# Больше всего мальчиков в классе 3c
# Больше всего девочек в классе 2a
print ("Больше всего мальчиков в классе", max_info['class_male'], "их", max_info['male_count'])
print ("Больше всего девочек в классе", max_info['class_female'], "их", max_info['female_count'])