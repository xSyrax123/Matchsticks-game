from collections import deque


def matchsticks_str(matchsticks):
    x, y = divmod(matchsticks, 5)
    return '||||| '*x + '|'*y


def get_move(player, matchsticks):
    max_value = min(3, matchsticks)
    while True:
        try:
            value = int(input(f'{player} removes matchsticks: '))

            if 1 <= value <= max_value:
                return value
            else:
                print(f'You can delete only between 1 and {max_value} matchsticks.')
        except ValueError:
            print('The value entered is invalid. You can only enter numeric values.')


def main(matchsticks=23):
    players = deque(['Player 1', 'Player 2'])
    print('Game starts.')

    while matchsticks > 0:
        print(matchsticks_str(matchsticks))
        player = players[0]
        matchsticks -= get_move(player, matchsticks)
        players.rotate()

    print(f'{player} is eliminated.')


if __name__ == '__main__':
    main()
