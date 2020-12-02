# This program will write YOUR list of games to a .csv file
def write_games(filename, game_list):
    with open(filename, 'w') as file:
        for game in game_list:
            if game == game_list[-1]:
                file.write(game)
            else:
                file.write("{}," .format(game))
