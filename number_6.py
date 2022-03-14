# 6. Необходимо создать (не программно) текстовый файл,
# где каждая строка описывает учебный предмет и наличие лекционных,
# практических и лабораторных занятий по этому предмету и их количество.
# Важно, чтобы для каждого предмета не обязательно были все типы занятий.
# Сформировать словарь, содержащий название предмета и общее количество занятий по нему.
# Вывести словарь на экран.

# Примеры строк файла: Информатика: 100(л) 50(пр) 20(лаб).
# Физика: 30(л) — 10(лаб)
# Физкультура: — 30(пр) —
# Пример словаря: {“Информатика”: 170, “Физика”: 40, “Физкультура”: 30}

import re

lessons_dict = {}
with open('number_6.txt','r') as file:
    for line in file.readlines():
        key = re.split(' ', line)[0][:-1]
        try:
            lections = int(re.split(' ', line)[1][:-3])
        except ValueError:
            lections = 0
        try:
            practics = int(re.split(' ', line)[2][:-4])
        except ValueError:
            practics = 0
        try:
            labs = int(re.split(' ', line)[3][:-6])
        except ValueError:
            labs = 0
        lessons_dict[key] = lections + practics + labs

print(lessons_dict)