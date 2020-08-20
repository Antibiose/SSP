import random
picks = ["Stein", "Schere","Papier  "]

def computer_pick_print(computer_picks):
    print("Der Computer wählt "+ (computer_picks))

def player_loses():
    print("Du verlierst! :(")

def player_wins():
    print("Du gewinst! :)")
    

print("Schere, Stein, Papier Action - whoop!")
player_picks = input("Schere, Stein oder Papier? - Bitte großschreiben: ")
print("Du hast " + player_picks + " gewählt.")
computer_picks = random.choice(picks)


# computer/player draw
if player_picks == computer_picks:
    computer_pick_print(computer_picks)
    print("Unentschieden!")

# computer chooses rock
elif computer_picks == "Stein":
    computer_pick_print(computer_picks)                                                    
    if player_picks == "Schere":
        player_loses()
    else:
        player_wins()

#computer chooses scissors
elif computer_picks == "Schere":   
    computer_pick_print(computer_picks)                                                 
    if player_picks == "Papier":
        player_loses()
    else:
        player_wins()

#computer chooses Paper
else:
    if player_picks == "Stein":
        player_loses()
    else:
        player_wins()                                            
    