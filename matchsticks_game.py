class MatchsticksGame:
    def __init__(self):
        self.matchsticks = 23
        self.player2 = False


    def __is_valid_input(self, player):
        return True if 1 <= player <= 3 else False
            

    def __show_matchsticks(self):
        return '||||| '*(self.matchsticks//5) + '|'*(self.matchsticks%5)


    def __game_finish(self):
        return True if self.matchsticks <= 0 else False
        

    def play(self):
        print('Game starts')
        print(self.__show_matchsticks())

        while True:
            player = int(input(f'The player {self.player2+1} remove: '))

            if not self.__is_valid_input(player):
                print('You can delete only between 1 and 3 matchsticks.')
                continue

            self.matchsticks -= player
            print(self.__show_matchsticks())

            if self.__game_finish():
                print(f'The player {self.player2+1} is eliminated.')
                break

            self.player2 = not self.player2


if __name__ == '__main__':
    game = MatchsticksGame()
    game.play()