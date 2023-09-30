board = list(range(1, 10))


def board_draw():
    print('-------------')
    for i in range(3):
        print('|', board[0 + i * 3], '|', board[1 + i * 3], '|', board[2 + i * 3], '|')
    print('-------------')


def get_input():
    while True:
        value = input('В какую ячейку поставить символ X: ')
        value = int(value)
        board[value - 1] = 'X'
        break


def main():
    while True:
        board_draw()
        get_input()


if __name__ == '__main__':
    main()
