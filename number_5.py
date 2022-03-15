#5. Создать (программно) текстовый файл, записать в него программно набор чисел, разделенных пробелами.
# Программа должна подсчитывать сумму чисел в файле и выводить ее на экран.
import re

from random import randrange

with open('number_5.txt', 'w') as file_to_write:
    random_list = [randrange(-1000, 1000) for i in range(20)]
    print(" ".join(map(str, random_list)), file = file_to_write)

with open('number_5.txt', 'r') as file_to_read:
    numbers = file_to_read.read().split()
    print(sum(float(x)for x in numbers))