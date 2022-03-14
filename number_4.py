# Создать (не программно) текстовый файл со следующим содержимым:

#One — 1
#Two — 2
#Three — 3
#Four — 4

# Необходимо написать программу, открывающую файл на чтение и считывающую построчно данные.
# При этом английские числительные должны заменяться на русские.
# Новый блок строк должен записываться в новый текстовый файл.

import re

with open('number_4_for_read.txt', 'r') as file_to_read:
    with open('number_4_for_write.txt', 'w') as file_to_write:
        for line in file_to_read.readlines():
            if line[-1] == '\n':
                if re.split(' ', line)[0] == 'One':
                    new_line = 'Один' + ' ' + re.split(' ', line)[1] + ' ' + re.split(' ', line)[2][:-1]
                    print(new_line, file=file_to_write)
                elif re.split(' ', line)[0] == 'Two':
                    new_line = 'Два' + ' ' + re.split(' ', line)[1] + ' ' + re.split(' ', line)[2][:-1]
                    print(new_line, file=file_to_write)
                elif re.split(' ', line)[0] == 'Three':
                    new_line = 'Три' + ' ' + re.split(' ', line)[1] + ' ' + re.split(' ', line)[2][:-1]
                    print(new_line, file=file_to_write)
            else:
                new_line = 'Четыре' + ' ' + re.split(' ', line)[1] + ' ' + re.split(' ', line)[2]
                print(new_line, file=file_to_write)