# Задача-1:
# Дан список фруктов.
# Напишите программу, выводящую фрукты в виде нумерованного списка,
# выровненного по правой стороне.
# Пример:
# Дано: ["яблоко", "банан", "киви", "арбуз"]
# Вывод:
# 1. яблоко
# 2.  банан
# 3.   киви
# 4.  арбуз
# Подсказка: воспользоваться методом .format()

fruits = ['яблоко', 'груша', 'банан', 'персик', 'абрикос', 'киви', 'апельсин']
max_length = 0
number = 1

for fruit in fruits:
    if len(fruit) > max_length:
        max_length = len(fruit)

# .rjust()
for fruit in fruits:
    print(str(number) + '. ' + fruit.rjust(max_length))
    number += 1

# .format()
print('_' * (max_length * 2))
number = 1
for fruit in fruits:
    print('{0}. {1:>{2}}'.format(number, fruit, max_length))
    number += 1

# f-строки
print('_' * (max_length * 2))
number = 1
for fruit in fruits:
    print(f'{number}. {fruit:>{max_length}}')
    number += 1

# Задача-2:
# Даны два произвольные списка.
# Удалите из первого списка элементы, присутствующие во втором списке.

# пустая строка + отделяющая линия
print()
print('_' * 100)
print()

list1 = [100, 200, 222, 300, 400, 500, 600, 666, 700, 800, 888, 900]
list2 = [111, 222, 333, 444, 555, 666, 777, 888, 999]

print('Первый список: ', list1)
print('Второй список: ', list2)

# решение через множества:
new_list1 = list(set(list1) - set(list2))
print('Отредактированный первый список: ', new_list1)

# решение через операции со списками:
for a in list1:
    if a in list2:
        list1.remove(a)
print('Отредактированный первый список: ', list1)


# Задача-3:
# Дан произвольный список из целых чисел.
# Получите НОВЫЙ список из элементов исходного, выполнив следующие условия:
# если элемент кратен двум, то разделить его на 4, если не кратен, то умножить на два.

# пустая строка + отделяющая линия
print()
print('_' * 100)
print()

list_of_numbers = [100, 200, 222, 300, 333, 400, 500, 555, 600, 700, 800, 888, 900, 999]
print('Исходный список: ', list_of_numbers)

new_list_of_numbers = []
for number in list_of_numbers:
    if number % 2 == 0:
        new_list_of_numbers.append(number / 4)
    else:
        new_list_of_numbers.append(number * 2)

# необязательное удаление 0 после запятой
for i in range(len(new_list_of_numbers)):
    if new_list_of_numbers[i] % 1 == 0:
        new_list_of_numbers[i] = int(new_list_of_numbers[i])

print('Новый список: ', new_list_of_numbers)