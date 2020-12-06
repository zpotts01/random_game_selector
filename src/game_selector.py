import os
import csv
import time


class GameSelector:
    version = 0.0
    fpath = os.path.join("data", "game_list.csv")
    list_of_games = []

    def get_list_of_games(self):
        return self.list_of_games

    def read_games(self):
        """
        This method reads games from a .csv file and adds them to list_of_games
        :return: none
        """
        with open(self.fpath, 'rt') as file:
            reader = csv.reader(file)
            for line in reader:
                for game_str in line:
                    self.list_of_games.append(game_str)

    def write_games(self):
        """
        This method writes games to a .csv file
        :return: none
        """
        with open(self.fpath, 'w') as file:
            for game in self.list_of_games:
                if game == self.list_of_games[-1]:
                    file.write(game)
                else:
                    file.write("{},".format(game))

    def __str__(self):
        rtn_str = ""
        if len(self.list_of_games) < 11:
            for i in range(0, len(self.list_of_games)):
                rtn_str += "{}: {}\n".format(i + 1, self.list_of_games[i])
        else:
            half_1 = self.list_of_games[:len(self.list_of_games)//2]
            half_2 = self.list_of_games[len(self.list_of_games)//2:]
            for i in range(0, len(self.list_of_games)//2):
                rtn_str += "{}: {}{}|  {}: {}\n" .format(i+1, half_1[i], " "*(37 - len(half_1[i])), i +
                                                         (len(self.list_of_games)//2 + 1), half_2[i])
        return rtn_str


if __name__ == "__main__":
    print("This program randomly selects a game from your provided list of games.\n"
          "It is designed to help you decide what to play when you are short on time and can't make up your mind!\n")
    game_selector = GameSelector()
    game_selector.read_games()
    game_list = game_selector.get_list_of_games()
    if len(game_list) > 0:
        print("Here is the current list of games:")
        print(game_selector)

    # game_in = input("Please enter the name of a game ('q' to quit):\n")
    # while game_in.lower() != "q":
    #     list_of_games.append(game_in)
    #     print("Added {} to the list!" .format(game_in))
    #     game_in = input("Please enter the name of a game ('q' to quit):\n")
    #
    # print("Thank you for the list of games!")
    # print("Here is the list:\n{}" .format(list_of_games))
    # edit = input("Would you like to add or remove any games from the list? (Y/N)\n")
    # if edit.lower() != "n":
    #     choice = input("Would you like to add or remove a game? (A/R)\n")
    #     while choice.lower() not in ["a", "r"]:
    #         print("Oy!")
    #         choice = input("Would you like to add or remove a game? (A/R)\n")
