class MatchsticksGame:
    def __init__(self):
        self.matchsticks = 23
        self.player2 = False


    def _is_valid_input(self, player):
        return 1 <= player <= 3
            

    def _show_matchsticks(self):
        return '||||| '*(self.matchsticks//5) + '|'*(self.matchsticks%5)


    def _game_finish(self):
        return self.matchsticks <= 0
        

    def play(self):
        print('Game starts')
        print(self._show_matchsticks())

        while True:
            player = int(input(f'The player {self.player2+1} remove: '))

            if not self._is_valid_input(player):
                print('You can delete only between 1 and 3 matchsticks.')
                continue

            self.matchsticks -= player
            print(self._show_matchsticks())

            if self._game_finish():
                print(f'The player {self.player2+1} is eliminated.')
                break

            self.player2 = not self.player2


if __name__ == '__main__':
    game = MatchsticksGame()
    game.play()
