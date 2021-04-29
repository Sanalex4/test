import random
import RPG_mod as Mod
from RPG_mod import Player_1 as Pl1
from RPG_mod import Player_2 as Pl2


def main(p1, p2, hp,):
    p1.PrintDescription()
    p2.PrintDescription()
    print()
    print('Ход ', p1.Name, ':')
    Mod.PrintMoves()
    move = input()
    Mod.PrintDivision()
    if move == '1':
        percent = random.randint(1, 100)
        if percent <= 70:
            damage = random.randint(10, 25)
            print('Урон: -', damage, ' HP')
            p2.HP -= damage
        elif 70 < percent <= 90:
            print('Крит удар :D')
            damage = random.randint(26, 35)
            print(' Урон: -', damage, ' HP')
            p2.HP -= damage
        elif 90 < percent < 99:
            print('Промах :(')
        else:
            print('Ваншот')
            damage = hp
            print(' Урон: -', damage, ' HP')
            p1.HP -= damage
    elif move == '2':
        if p1.SpAttacks > 0:
            damage = random.randint(25, 40)
            print('Урон: -', damage, ' HP')
            p2.HP -= damage
            p1.SpAttacks -= 1
        else:
            print('Нет спец атак, пропуск хода')
    elif move == '3':
        if p1.Hills > 0:
            hill = random.randint(30, 50)
            print('Лечение: +', hill)
            if p1.HP > hp:
                p1.HP = hp
            p1.HP += hill
            p1.Hills -= 1
        else:
            print('Нет аптечек, пропуск хода')
    else:
        print('Нет такого действия, пропуск хода')


HP = Mod.hp_input(0)
SP = Mod.sp_input(-1)
hills = Mod.hills_input(-1)
f_name = Mod.f_name_input()
s_name = Mod.s_name_input()

switch = random.randint(1, 2)
if switch == 1:
    name_1 = f_name
    name_2 = s_name
else:
    name_1 = s_name
    name_2 = f_name
player_1 = Pl1(name_1, HP, SP, hills)
player_2 = Pl2(name_2, HP, SP, hills)
Mod.PrintDivision()

while True:
    if player_1.HP < 0 or player_2.HP < 0:
        break
    main(player_1, player_2, HP)
    if player_1.HP < 0 or player_2.HP < 0:
        break
    main(player_2, player_1, HP)

print()
if player_1.HP <= 0:
    print('Победил ', player_2.Name)
elif player_2.HP <= 0:
    print('Победил ', player_1.Name)
print()
input('Нажмите любую клавишу, чтобы продолжить')
