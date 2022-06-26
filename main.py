# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
from typing import Any, List


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
#1. Создать список и заполнить его элементами различных типов данных. Реализовать скрипт проверки типа данных каждого элемента. Использовать функцию type() для проверки типа.
# Элементы списка можно не запрашивать у пользователя, а указать явно, в программе.
the_list = [4, 19.5, "genetic", None]
a = 4
b = 19.5
c = "genetic"
d = None
print (type(a))
print (type(b))
print (type(c))
print (type(d))


#2. Для списка реализовать обмен значений соседних элементов. Значениями обмениваются элементы с индексами 0 и 1, 2 и 3 и т. д.
s = [1, 2, 3, 4, 5, 6]
s[0] = 2
s[1] = 1
s[2] = 3
s[3] = 2
s[4] = 6
s[5] = 5
print (s)


# При нечётном количестве элементов последний сохранить на своём месте. Для заполнения списка элементов нужно использовать функцию input().
#3. Пользователь вводит месяц в виде целого числа от 1 до 12. Сообщить, к какому времени года относится месяц (зима, весна, лето, осень). Напишите решения через list и dict.
month = int(input("Введите номер месяца "))
seas_list = ['winter', 'spring', 'summer', 'autumn']
seas_dict = {0 : 'winter', 1 : 'spring', 2 : 'summer', 3 : 'autumn'}

if month == 1 or month == 12 or month == 2:
        print(seas_dict.get(0))
        print(seas_list[0])
elif month == 3 or month == 4 or month == 5:
    print(seas_dict.get(1))
    print(seas_list[1])
elif month == 6 or month == 7 or month == 8:
    print(seas_dict.get(2))
    print(seasons_list[2])

elif month == 9 or month == 10 or month == 11:
    print(seas_dict.get(3))
    print(seas_list[3])









#4. Пользователь вводит строку из нескольких слов, разделённых пробелами. Вывести каждое слово с новой строки. Строки нужно пронумеровать.
# Если слово длинное, выводить только первые 10 букв в слове.

a_str = input("Введите данные ")
a = str.split(' ')
for i, el in enumerate(a, 1):
    if len(el) > 10:
        el = el [0:10]
    print(f"{i}. - {el}")

#5. Реализовать структуру «Рейтинг», представляющую собой набор натуральных чисел, который не возрастает. У пользователя нужно запрашивать новый элемент рейтинга.
# Если в рейтинге существуют элементы с одинаковыми значениями, то новый элемент с тем же значением должен разместиться после них.
#Подсказка. Например, набор натуральных чисел: 7, 5, 3, 3, 2.
#Пользователь ввёл число 3. Результат: 7, 5, 3, 3, 3, 2.
#Пользователь ввёл число 8. Результат: 8, 7, 5, 3, 3, 2.
#Пользователь ввёл число 1. Результат: 7, 5, 3, 3, 2, 1.
#Набор натуральных чисел можно задать сразу в коде, например, my_list = [7, 5, 3, 3, 2].
number = int(input("Enter number: "))
my_list = [7, 4, 3, 2]
c = my_list.count(number)
for element in my_list:
    if c > 0:
        i = my_list.index(number)
        my_list.insert(i+c, number)
        break
    else:
        if number > element:
            j = my_list.index(element)
            my_list.insert(j, number)
            break
        elif number < my_list[len(my_list) - 1]:
            my_list.append(number)


#6. * Реализовать структуру данных «Товары». Она должна представлять собой список кортежей. Каждый кортеж хранит информацию об отдельном товаре.
# В кортеже должно быть два элемента — номер товара и словарь с параметрами, то есть характеристиками товара: название, цена, количество, единица измерения.
# Структуру нужно сформировать программно, запросив все данные у пользователя.
#Пример готовой структуры:

#[
#(1, {“название”: “компьютер”, “цена”: 20000, “количество”: 5, “eд”: “шт.”}),
#(2, {“название”: “принтер”, “цена”: 6000, “количество”: 2, “eд”: “шт.”}),
#(3, {“название”: “сканер”, “цена”: 2000, “количество”: 7, “eд”: “шт.”})
#]
#Нужно собрать аналитику о товарах. Реализовать словарь, в котором каждый ключ — характеристика товара, например, название.
# Тогда значение — список значений-характеристик, например, список названий товаров.
#Пример:
#{
#“название”: [“компьютер”, “принтер”, “сканер”],
#“цена”: [20000, 6000, 2000],
#“количество”: [5, 2, 7],
#“ед”: [“шт.”]
#}

number = int (input ("Введите номер продукта: "))
prod = []
features = {}
value1 = input (str ("Название товара"))
value2 = input (str ("Цена"))
value3 = input (str ("Количество"))
value4 = input (str("Единицы измерения"))


features["Название товара"] = value1
features["Цена"] = value2
features["Количество"] = value3
features["Единицы измерения"] = value4
prod.append(tuple[number,features])
print(prod)





