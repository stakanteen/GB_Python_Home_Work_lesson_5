#5. Создать (программно) текстовый файл, записать в него программно набор чисел, разделенных пробелами.
# Программа должна подсчитывать сумму чисел в файле и выводить ее на экран.

from random import randint

with open('number_5.txt', 'w') as file_to_write:
    random_list = [randint(-1000, 1000) for i in range(20)]
    print(" ".join(map(str, random_list)), file = file_to_write)