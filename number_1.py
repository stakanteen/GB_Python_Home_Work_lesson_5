# 1. Создать программно файл в текстовом формате, записать в него построчно данные,
# вводимые пользователем. Об окончании ввода данных свидетельствует пустая строка.

write_indicator = 1
string_to_write = []

while write_indicator == 1:
    string = input('Введите строку для записи. Для прекращения оставьте строку пустой: ')
    string_to_write.append(string)
    if string == '':
        write_indicator = 0

with open('result.txt', 'a+') as file_to_write:
    for string_ in string_to_write:
        print(string_, file = file_to_write)