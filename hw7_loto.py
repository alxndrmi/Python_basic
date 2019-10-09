"""
== Лото ==
Правила игры в лото.
Игра ведется с помощью специальных карточек, на которых отмечены числа,
и фишек (бочонков) с цифрами.
Количество бочонков — 90 штук (с цифрами от 1 до 90).
Каждая карточка содержит 3 строки по 9 клеток. В каждой строке по 5 случайных цифр,
расположенных по возрастанию. Все цифры в карточке уникальны. Пример карточки:
--------------------------
    9 43 62          74 90
 2    27    75 78    82
   41 56 63     76      86
--------------------------
В игре 2 игрока: пользователь и компьютер. Каждому в начале выдается
случайная карточка.
Каждый ход выбирается один случайный бочонок и выводится на экран.
Также выводятся карточка игрока и карточка компьютера.
Пользователю предлагается зачеркнуть цифру на карточке или продолжить.
Если игрок выбрал "зачеркнуть":
	Если цифра есть на карточке - она зачеркивается и игра продолжается.
	Если цифры на карточке нет - игрок проигрывает и игра завершается.
Если игрок выбрал "продолжить":
	Если цифра есть на карточке - игрок проигрывает и игра завершается.
	Если цифры на карточке нет - игра продолжается.

Побеждает тот, кто первый закроет все числа на своей карточке.
Пример одного хода:
Новый бочонок: 70 (осталось 76)
------ Ваша карточка -----
 6  7          49    57 58
   14 26     -    78    85
23 33    38    48    71
--------------------------
-- Карточка компьютера ---
 7 11     - 14    87
      16 49    55 77    88
   15 20     -       76  -
--------------------------
Зачеркнуть цифру? (y/n)
Подсказка: каждый следующий случайный бочонок из мешка удобно получать
с помощью функции-генератора.
Подсказка: для работы с псевдослучайными числами удобно использовать
модуль random: http://docs.python.org/3/library/random.html
"""

import random


class Player:
    def __init__(self, name):
        self.lines = 3
        self.columns = 9
        self.numbers_in_column = 5
        self.num_limit = 90
        self.name = name
        self.card = [['  ', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '  '],
                     ['  ', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '  '],
                     ['  ', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '  ']]
        self.make_card()

    def make_card(self):
        card_numbers = []

        for i in range(1, self.num_limit + 1):
            card_numbers.append(i)
        random.shuffle(card_numbers)

        a = 0
        while a < self.lines:
            position = [i for i in range(self.columns)]
            random.shuffle(position)
            pos = [position.pop(0) for _ in range(self.numbers_in_column)]
            pos.sort()
            card_line = [card_numbers.pop(0) for _ in range(self.numbers_in_column)]
            card_line.sort()
            for b in pos:
                self.card[a][b] = str(card_line.pop(0))
            a += 1

        card = ''
        for a in range(self.lines):
            for b in range(self.columns):
                card = card + str(self.card[a][b]).rjust(4)
            card = card + '\n'
        self.print_card = f'Карточка игрока: {self.name}\n{card}'
        return self.print_card


class Game:
    def __init__(self, number):
        self.lines = 3
        self.columns = 9
        self.numbers_in_column = 5
        self.num_limit = 90
        self.number = number
        self.nums_bag()
        self.game_start()

    def nums_bag(self):
        self.bag = []
        for i in range(1, self.num_limit + 1):
            self.bag.append(str(i))
        random.shuffle(self.bag)
        return self.bag

    def game_start(self):
        print(player.print_card)
        print(computer.print_card)

        for number in self.bag:
            player_answer = input(f'Достали число: {number}, Зачеркнуть? (y/n)\n')

            is_number_in_card = None

            if player_answer == 'y':
                for i in range(self.lines):
                    is_number_in_card = number in player.card[i]
                    if is_number_in_card:
                        player.card[i][player.card[i].index(number)] = '--'
                        print(self.str_card(player))
                        # print(self.str_card(computer))
                        break
                if not is_number_in_card:
                    print('В вашей карте нет выпавшего числа. Вы проиграли!')
                    break

            is_number_in_card = None

            if player_answer == 'n':
                for i in range(self.lines):
                    is_number_in_card = number in player.card[i]
                    if is_number_in_card:
                        print('В вашей карте есть выпавшее число. Вы проиграли!')
                        break
                if is_number_in_card:
                    break
                else:
                    print(self.str_card(player))
                    # print(self.str_card(computer))

            if player_answer != 'n' and player_answer != 'y':
                print('Ошибка ввода')
                break

            for i in range(self.lines):
                is_number_in_card = number in computer.card[i]
                if is_number_in_card:
                    computer.card[i][computer.card[i].index(number)] = '--'
                    break
                else:
                    continue
            print(self.str_card(computer))

            check1 = 0
            check2 = 0
            for a in range(1, self.num_limit + 1):
                for b in range(self.lines):
                    if str(a) in player.card[b]:
                        check1 = 1
                    if str(a) in computer.card[b]:
                        check2 = 1
            if check1 == 0:
                print(f'Игрок {player.name} победил!')
                break
            elif check2 == 0:
                print(f'Игрок {computer.name} победил!')
                break

    def str_card(self, player):
        card = ''
        for i in range(self.lines):
            for j in range(self.columns):
                card = card + str(player.card[i][j]).rjust(4)
            card = card + '\n'
        return f'Карточка игрока: {player.name}\n{card}'


player = Player(input('Введите имя игрока: '))
computer = Player('Компьютер')
Game(1)
while True:
    play_again = input('Хотите сыграть ещё раз?(y/n)')
    if play_again == 'y':
        player = Player(input('Введите имя игрока: '))
        computer = Player('Компьютер')
        Game(1)
    else:
        print('\nИгра закончена.')
        break