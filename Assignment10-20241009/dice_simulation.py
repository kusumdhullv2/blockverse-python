import random

def roll_dice():
    return random.randint(1, 6)

input('Dice Simulation Game!!! Press any key to start.')

while True:

    outcome = roll_dice()
    count = 0
    if outcome == 6:
        while(count < 2):
            input(f"You got {outcome}, press any key to roll again ")
            outcome = roll_dice()
            if(outcome != 6):
                print(f"you got {outcome} ")
                break
            count += 1
    else:
        print(f"you got {outcome} ")

    perm = input("Do you want to play again?(y/n) ").lower()
    
    if perm == 'n':
        print("see you next time!!! ")
        break
