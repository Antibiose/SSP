import random

player_pick = "Stein"
pick_list = ["Stein", "Schere", "Papier"]

a = random.choice(pick_list)

if player_pick == a:
    print(a)
    print("Unentschieden")
else:
    print("negativtest")
    print(a)