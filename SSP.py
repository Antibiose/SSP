import random
import time



picks = ["Stein", "Schere","Papier"]
player_entry = ["Stein", "Schere","Papier"]


def :
    print("Der Computer wählt "+ (computer_picks)); time.sleep(0.5)

def player_loses():
    time.sleep(0.5)
    print("Du verlierst! :(")

def player_wins():
    time.sleep(0.5)
    print("Du gewinnst! :)")

#just for drama purposes - actual ppl do say that when playing
def game_drama():
    print("SCHERE!"); time.sleep(0.5)
    print("STEIN!"); time.sleep(0.5)
    print("PAPIER!"); time.sleep(0.1)

    

print("Schere, Stein, Papier Action - whoop!"); time.sleep(1)
player_picks = ""
while player_picks not in player_entry:
    player_picks = input("Schere, Stein oder Papier? - Bitte großschreiben: ") 

game_drama()


print("Du hast " + player_picks + " gewählt.") 
computer_picks = random.choice(picks)
computer_pick_print(computer_picks); time.sleep(0.5)


# computer/player draw
if player_picks == computer_picks:
    
    print("Unentschieden!")

# computer chooses rock
elif computer_picks == "Stein":
                                                        
    if player_picks == "Schere" or player_picks == "schere":
        player_loses()
    else:
        player_wins()
jkgsdhk
#computer chooses scissors
elif computer_picks == "Schere":   
                                                     
    if player_picks == "Papier" or player_picks == "papier":
        player_loses()
    else:
        player_wins()

#computer chooses Paper
else:
    if player_picks == "Stein" or player_picks == "stein":
            
        player_loses()
    else:
        player_wins()                                            