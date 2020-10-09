import random

rounds = int(input("How many rounds would you like to play: "))
while rounds > 0:
    # 0 = rock; 1 = paper; 2 = scissors
    my_number = random.randint(0, 2)
    my_result = ["Rock", "Paper", "Scissors"][my_number]
    your_result = input("Which do you choose: [R/P/S] ")
    your_number = ['R', 'P', 'S'].index(your_result)
    print("I chosed: " + my_result)
    if my_number == your_number + 1: print("I win!")
    elif my_number == your_number: print("Even")
    else: print("You win!")
    rounds -= 1
print("Finished")