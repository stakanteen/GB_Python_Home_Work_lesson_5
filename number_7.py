# 7. Создать вручную и заполнить несколькими строками текстовый файл,
# в котором каждая строка должна содержать данные о фирме: название, форма собственности, выручка, издержки.

# Пример строки файла: firm_1 ООО 10000 5000.

# Необходимо построчно прочитать файл, вычислить прибыль каждой компании, а также среднюю прибыль.
# Если фирма получила убытки, в расчет средней прибыли ее не включать.

# Далее реализовать список. Он должен содержать словарь с фирмами и их прибылями, а также словарь
# со средней прибылью. Если фирма получила убытки, также добавить ее в словарь (со значением убытков).

# Пример списка: [{“firm_1”: 5000, “firm_2”: 3000, “firm_3”: 1000}, {“average_profit”: 2000}].

# Итоговый список сохранить в виде json-объекта в соответствующий файл.

# Пример json-объекта:

# [{"firm_1": 5000, "firm_2": 3000, "firm_3": 1000}, {"average_profit": 2000}]

# Подсказка: использовать менеджер контекста.
import json
import re
profit_dict = {}
avg_profit = {}
final_list = []
with open('number_7_read.txt', 'r') as file:
    avg_list = []
    for line in file.readlines():
        key_ = re.split(' ', line)[0]
        profit_ = float(re.split(' ', line)[2]) - float(re.split(' ', line)[3])
        profit_dict[key_] = profit_
        if profit_ >= 0:
            avg_list.append(float(re.split(' ', line)[2]) - float(re.split(' ', line)[3]))
        else:
            avg_list.append(0)
    avg_profit['average_profit'] = round(sum(avg_list)/len(avg_list), 2)
    final_list.append(profit_dict)
    final_list.append(avg_profit)
    with open ('number_7_write.txt', 'w') as file_write:
        print(json.dumps(final_list, ensure_ascii=False), file = file_write)