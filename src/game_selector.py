# This program uses __ to select a random game from a list
import os
import time
from src.write_game_list import write_games
from src.read_game_list import read_games

if __name__ == "__main__":
    fpath = os.path.join("data", "game_list.csv")
    list_of_games = []
    game_in = input("Please enter the name of a game:\n")
    while game_in.lower() != "q":
        list_of_games.append(game_in)
        print("Added {} to the list!" .format(game_in))
        game_in = input("Please enter the name of a game:\n")

    print("Thank you for the list of games!")
    print("Here is the list:\n{}" .format(list_of_games))
    edit = input("Would you like to add or remove any games from the list? (Y/N)\n")
    if edit.lower() != "n":
        choice = input("Would you like to add or remove a game? (A/R)\n")
        while choice.lower() not in ["a", "r"]:
            print("Oy!")
            choice = input("Would you like to add or remove a game? (A/R)\n")
