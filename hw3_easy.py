# Постарайтесь использовать то, что мы прошли на уроке при решении этого ДЗ,
# вспомните про zip(), map(), lambda, посмотрите где лучше с ними, а где они излишни!

# Задание - 1
# Создайте функцию, принимающую на вход Имя, возраст и город проживания человека
# Функция должна возвращать строку вида "Василий, 21 год(а), проживает в городе Москва"


def info(name, age, city):
    return f'{name}, {age} год(а), проживает в городе {city}'


print(info('Иван', '21', 'Москва'))


# Задание - 2
# Создайте функцию, принимающую на вход 3 числа, и возвращающую наибольшее из них


def max_of_three(a, b, c):
    numbers = (a, b, c)
    max_number = 0
    for number in numbers:
        if number > max_number:
            max_number = number
    return max_number


print(max_of_three(-100, 11, 1000.555))

# Задание - 3
# Создайте функцию, принимающую неограниченное количество строковых аргументов,
# верните самую длинную строку из полученных аргументов


def longer_line(*args):
    max_len = ''
    for arg in args:
        if len(arg) >= len(max_len):
            max_len = arg
    return max_len


print(longer_line('A', 'BB', 'CCCCC', 'Dd Ddd Dddd', 'ZZZZZZZZZZZZZZZZZZZ'))