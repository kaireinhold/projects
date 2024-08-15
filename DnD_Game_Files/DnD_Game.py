import rollDice
import time

while True:
    dice_Q = input("Would you like to roll a dice? ").lower().strip()
    if dice_Q == "yes":
        rollDice.roll()
        time.sleep(1)
    elif dice_Q == "no":
        print("ok")
        time.sleep(1)
        break
        
