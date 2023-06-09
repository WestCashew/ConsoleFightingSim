from battle import fight
from setup import loading_players_dialogue, setting_up_players, saving_players_dialogue, stat_checking
from sys import exit
# todo done for now, maybe improve saving logic

print("BATTLE sim by SB")
file = 'players.pickle'
# creating 2 players with this function
def player_loading_player_creation():
    load_or_new_players = input("Do you want to load old players or create new ones? typ load or new: ")
    if "new" in load_or_new_players:
        p1, p2 = setting_up_players("2")
    else:
        amount_of_loads = str(input("do you want to load 1 or 2 players: "))
        if "1" in amount_of_loads:
            p1 = loading_players_dialogue(file)
            x, p2 = setting_up_players(amount_of_loads)
        else:
            p1 = loading_players_dialogue(file)
            p2 = loading_players_dialogue(file)
    return p1, p2



def main():
    p1, p2 = player_loading_player_creation()
    # saving the beginning state of the players (after the battle their health is different)
    p1_reserve = p1
    p2_reserve = p2
    stat_checking(p1, p2)
    print("")
    fight(p1, p2)
    saving_players_dialogue(p1_reserve, p2_reserve, file)
    exit_or_repeat = input("Do you want to exit or do you want to play again? typ exit or just hit enter: ")
    if exit_or_repeat == "exit":
        return False
    else:
        return True


def full_game():
    running = True
    while running:
        main_function = main()
        if not main_function:
            running = False
            exit()


full_game()


