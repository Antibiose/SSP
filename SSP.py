import random

picks = ["Stein", "Schrere", "Papier"]


    

print("Schere, Stein, Papier Action - whoop!")
player_picks = input("Schere, Stein oder Papier? - Bitte großschreiben")
computer_picks =  random.choice(picks)
print(computer_picks)

if player_picks == computer_picks:
    print(computer_picks)
    print("Du hast " + player_picks + " gewählt und der Computer " + computer_picks)
    print("Unentschieden!")
else:
    print(computer_picks)
    print("Testende")
 