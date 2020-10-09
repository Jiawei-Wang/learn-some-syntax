import random
mine = random.randint(0, 2)
yours = input("Which do you choose: [R/P/S] ")
if yours == 'R':
    if mine == 0: print("even")
    elif mine == 1: print("I win")
    else: print("you win")
elif yours == 'P':
    if mine == 1: print("even")
    elif mine == 2: print("I win")
    else: print("you win")
else:
    if mine == 2: print("even")
    elif mine == 0: print("I win")
    else: print("you win")