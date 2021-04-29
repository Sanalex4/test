class Player:
    def __init__(self, name, hp, sp_attacks, hills):
        self.Name = name
        self.HP = hp
        self.SpAttacks = sp_attacks
        self.Hills = hills

    def PrintDescription(self):
        print()
        print(self.Name, ':')
        print('    Количество HP:', self.HP)
        print('    Количество спец атак: ', self.SpAttacks)
        print('    Количество аптечек: ', self.Hills)


def PrintMoves():
    print('    1 - обычная атака')
    print('    2 - спец атака')
    print('    3 - лечение')


def PrintDivision():
    print('--------------------------------------------')


class Player_1(Player):
    pass


class Player_2(Player):
    pass


def hp_input(hp):
    while hp <= 0:
        try:
            hp = int(input('Количество HP: '))
            if hp <= 0:
                print('Введено число меньше или равное нулю')
                hp = 0
        except ValueError:
            print('Введено неверное значение')
            hp = 0
    return hp


def sp_input(sp):
    while sp < 0:
        try:
            sp = int(input('Количество спец атак: '))
            if sp < 0:
                print('Введено число меньше нуля')
                sp = 0
        except ValueError:
            print('Введено неверное значение')
            sp = -1
    return sp


def hills_input(hills):
    while hills < 0:
        try:
            hills = int(input('Количество аптечек: '))
            if hills < 0:
                print('Введено число меньше нуля')
                hills = -1
        except ValueError:
            print('Введено неверное значение')
            hills = -1
    return hills


def f_name_input():
    while True:
        f_name = input('Имя первого игрока: ')
        if f_name:
            break
        else:
            print('Введена пустая строка')
    return f_name


def s_name_input():
    while True:
        s_name = input('Имя второго игрока: ')
        if s_name:
            break
        else:
            print('Введена пустая строка')
    return s_name
