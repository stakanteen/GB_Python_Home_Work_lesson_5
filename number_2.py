# 2. Создать текстовый файл (не программно), сохранить в нем несколько строк,
# выполнить подсчет количества строк, количества слов в каждой строке.

import re

with open('number_2.txt', 'r') as file_for_count:
    count_var = file_for_count.readlines()
    print('Количество строк в файле {}'.format(len(count_var)))
    i = 1
    for lines in count_var:
        print('В строке № {} находится {} слов'.format(i, len(re.split(' ',lines))))
        i += 1