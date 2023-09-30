board = list(range(1, 10))


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


def main():
    while True:
        board_draw()
        player_token = input('Выберите символ X или O: ')
        get_input(player_token)


if __name__ == '__main__':
    main()
