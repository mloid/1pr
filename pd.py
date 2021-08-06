import csv


#СОЗДАНИЕ НОВОЙ ТАБЛИЦЫ

#записываем данные в таблицу data
data = [['hostname', 'vendor', 'model', 'location'],
        ['sw1', 'Cisco', '3750', 'London, Best str'],
        ['sw2', 'Cisco', '3850', 'Liverpool, Better str'],
        ['sw3', 'Cisco', '3650', 'Liverpool, Better str'],
        ['sw4', 'Cisco', '3650', 'London, Best str']]
#пишем имя дока
tablename = 'tablename'
#сохраняем
with open(tablename+'.csv', 'w') as f:
    writer = csv.writer(f)
    for row in data:
        writer.writerow(row)
       
#ЧТЕНИЕ СТАРОЙ ТАБЛИЦЫ

with open('sw_data.csv') as f:
    reader = csv.reader(f)
    for row in reader:
        print(row)


#    _~_
#   (o o)
#  /  V  \
# /(  _  )\
#   ^^ ^^
