# Задача - 1
# Ранее мы с вами уже писали игру, используя словари в качестве
# структур данных для нашего игрока и врага, давайте сделаем новую, но уже с ООП
# Опишите базовый класс Person, подумайте какие общие данные есть и у врага и у игрока
# Не забудьте, что у них есть помимо общих аттрибутов и общие методы.
# Теперь наследуясь от Person создайте 2 класса Player, Enemy.
# У каждой сущности должы быть аттрибуты health, damage, armor
# У каждой сущности должно быть 2 метода, один для подсчета урона, с учетом брони противника,
# второй для атаки противника.
# Функция подсчета урона должна быть инкапсулирована
# Вам надо описать игровой цикл так же через класс.
# Создайте экземпляры классов, проведите бой. Кто будет атаковать первым оставляю на ваше усмотрение.


class Person:
    def __init__(self, name, health, damage, armor):
        self.name = name
        self.health = health
        self.damage = damage
        self.armor = armor

    def _calculate_damage(self, enemy_armor):
        return int(self.damage // enemy_armor)

    def attack(self, enemy_damage):
        self.health -= int(enemy_damage // self.armor)
        return self.health


class Player(Person):
    pass


class Enemy(Person):
    pass


player_1 = Player('Игрок 1', 100, 15, 1.5)
enemy_1 = Enemy('Игрок 2', 100, 22, 1.1)


class Battle:
    # первый атакующий указывается первым после self, второй атакующий указывается последним
    def __init__(self, player, enemy):
        self.player = player
        self.enemy = enemy
        print(f'Здоворье у {self.player.name} = {self.player.health}')
        print(f'Здоворье у {self.enemy.name} = {self.enemy.health}')

    def start_game(self):
        i = 1
        print('Битва начивается:')

        while self.player.health > 0 or self.enemy.health > 0:
            print('Ход', i, '-->')

            print(f'{self.player.name} нанес {self.enemy.name.split()[0]}у {self.enemy.name.split()[1]} '
                  f'{self.player._calculate_damage(self.enemy.armor)} единиц урона, у того осталось {self.enemy.attack(self.player.damage)}'
                  f' единиц жизни.')

            print(f'{self.enemy.name} нанес {self.player.name.split()[0]}у {self.enemy.name.split()[1]} '
                  f'{self.enemy._calculate_damage(self.player.armor)} единиц урона, у того осталось {self.player.attack(self.enemy.damage)}'
                  f' единиц жизни.')

            if self.player.health <= 0:
                print(f'{self.player.name} победил!')
            elif self.enemy.health <= 0:
                print(f'{self.enemy.name} победил!')

            i += 1


battle = Battle(player_1, enemy_1)
battle.start_game()
