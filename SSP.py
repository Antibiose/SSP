import random

print("Willkommmen zu Schrere, Stein, Papier - muhahaha")
spieler1 = input("Schere, Stein oder Papier?")

computer = ("Schere", "Stein", "Papier")

if spieler1 == random.choice(computer):
    print("Unentschieden!!")
else:
    print("Test")


def ComputerSSP(computer):
    computer_pick = random.choice(computer)
    print(computer_pick)

ComputerSSP(computer)