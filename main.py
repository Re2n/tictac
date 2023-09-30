board = list(range(1, 10))
wins_coordinates = [(1, 2, 3), (4, 5, 6), (7, 8, 9), (1, 4, 7), (2, 5, 8), (3, 6, 9), (1, 5, 9), (3, 5, 7)]


def board_draw():
    print('-------------')
    for i in range(3):
        print('|', board[0 + i * 3], '|', board[1 + i * 3], '|', board[2 + i * 3], '|')
    print('-------------')


def get_input(player_token):
    while True:
        value = input(f'В какую ячейку поставить символ {player_token}: ')
        if not (value in '123456789'):
            print('Ошибочный ввод. Повторите попытку.')
            continue
        value = int(value)
        if str(board[value - 1]) in 'XO':
            print('Эта клетка уже занята.')
            continue
        board[value - 1] = player_token
        break


def check_win():
    for each in wins_coordinates:
        if (board[each[0] - 1]) == (board[each[1] - 1]) == (board[each[2] - 1]):
            return board[each[1] - 1]
    else:
        return False


def main():
    while True:
        board_draw()
        winner = check_win()
        if winner:
            print(winner, ' выиграл')
            break
        player_token = input('Выберите символ X или O: ')
        get_input(player_token)


if __name__ == '__main__':
    main()
