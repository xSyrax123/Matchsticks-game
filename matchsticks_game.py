class MatchsticksGame:
    def __init__(self, players=('Player 1', 'Player 2'), initial_matchsticks=23):
        self.players = players
        self.player = None
        self.turn = 0
        self.matchsticks = initial_matchsticks

    def _current_player(self):
        return self.players[self.turn % 2]

    def _show_matchsticks(self):
        return '||||| '*(self.matchsticks//5) + '|'*(self.matchsticks%5)

    def get_move(self, player):
        while True:
            try:
                matchsticks_to_remove = int(input(f'{player} removes matchsticks: '))

                if 1 <= matchsticks_to_remove <= 3:
                    return matchsticks_to_remove

                print('You can delete only between 1 and 3 matchsticks.')
            except ValueError:
                print('The value entered is invalid. You can only enter numeric values.')

    def _play_turn(self):
        self.player = self._current_player()
        self.turn += 1

    def _game_finished(self):
        return self.matchsticks <= 0

    def play(self):
        print('Game starts.')
        print(self._show_matchsticks())

        while self.matchsticks > 0:
            self._play_turn()
            matchsticks_to_remove = self.get_move(self.player)
            self.matchsticks -= matchsticks_to_remove
            print(self._show_matchsticks())

            if self._game_finished():
                print(f'{self.player} is eliminated.')
                break


if __name__ == '__main__':
    game = MatchsticksGame()
    game.play()
