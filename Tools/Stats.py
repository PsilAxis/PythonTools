import random

player_name = input("Enter your Name: ")
Hp = random.randint(1,20)
ATK = random.randint(1,20)
DEF = random.randint(1,20)
SPD = random.randint(1,20)
SPECIAL = random.randint(1,20)

print('Welcome '+ player_name + '!', 'Current Hp:', Hp , 'ATK: ', ATK, 'DEF:', DEF, 'SPD:', SPD, 'SPECIAL:', SPECIAL)
