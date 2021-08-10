# https://pyneng.readthedocs.io/ru/latest/book/17_serialization/csv.html#id3

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
#в pandas более подходящий вариант
       
#ЧТЕНИЕ СТАРОЙ ТАБЛИЦЫ

with open('sw_data.csv') as f:
    reader = csv.reader(f)
    for row in reader:
        print(row)

        

# https://pandas.pydata.org/pandas-docs/stable/user_guide/merging.html

import pandas as pd

df1 = pd.DataFrame(
    {
        "A": ["A0", "A1", "A2", "A3"],
        "B": ["B0", "B1", "B2", "B3"],
        "C": ["C0", "C1", "C2", "C3"],
        "D": ["D0", "D1", "D2", "D3"],
    }, 
    index=[0, 1, 2, 3],
)

df2 = pd.DataFrame(
    {
        "A": ["A4", "A5", "A6", "A7"],
        "B": ["B4", "B5", "B6", "B7"],
        "C": ["C4", "C5", "C6", "C7"],
        "D": ["D4", "D5", "D6", "D7"],
    },
    index=[4, 5, 6, 7],
)

# чтобы добавилась строка номера должны не совпадать
# чтобы добавились столбцы надо чтобы совпадали номера столбцов

result = df1.append(df2) 

# сохранение таблицы в формате csv

data.to_csv('out.csv',index=False)

# прочитать csv таблицу

data = pd.read_csv('sw_data.csv')


#    _~_
#   (o o)
#  /  V  \
# /(  _  )\
#   ^^ ^^
