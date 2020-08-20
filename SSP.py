import random
import time
picks = ["Stein", "Schere","Papier"]

def computer_pick_print(computer_picks):
    
    print("Der Computer wählt "+ (computer_picks))

def player_loses():
    time.sleep(0.5)
    print("Du verlierst! :(")

def player_wins():
    time.sleep(0.5)
    print("Du gewinst! :)")

#just for drama purposes - actual ppl do say that when playing
def game_drama():
    print("SCHERE!"); time.sleep(0.5)
    print("STEIN!"); time.sleep(0.5)
    print("PAPIER!"); time.sleep(1)

    

print("Schere, Stein, Papier Action - whoop!"); time.sleep(1)
player_picks = ""
while player_picks not in picks:
    player_picks = input("Schere, Stein oder Papier? - Bitte großschreiben: ") 

game_drama()


print("Du hast " + player_picks + " gewählt.") 
computer_picks = random.choice(picks)


# computer/player draw
if player_picks == computer_picks:
    computer_pick_print(computer_picks); time.sleep(0.5)
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
    