# This program uses __ to select a random game from a list
import os
import time
from src.write_game_list import write_games
from src.read_game_list import read_games

if __name__ == "__main__":
    fpath = os.path.join("data", "game_list.csv")
    print("File Path: {}".format(fpath))
    # Testing write
    game_list = ["The Elder Scrolls V: Skyrim", "Fallout 4", "Forza Horizon 4"]
    write_games(fpath, game_list)
    time.sleep(5)
    # Testing read
    check_games = read_games(fpath)
