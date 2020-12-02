# This program will implement methods to get the list of games to choose from via the .csv file made by
# 'write_game_list.py'
import csv


def read_games(filename):
    game_list = []
    with open(filename, 'rt') as file:
        reader = csv.reader(file)
        for line in reader:
            print(line)
    return game_list
