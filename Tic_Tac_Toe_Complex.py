
def game_board(x: int) -> list:
    game_board_lst = []
    lst_temp = []
    for i in range(x):
        lst_temp.append(str(i)+' ')

    game_board_lst.append(lst_temp)

    game_board_lst[0][0] = ' '

    for i in range(x - 1):
        lst_temp = ['_|'] * x
        lst_temp[0] = str(i + 1)
        game_board_lst.append(lst_temp)

    return game_board_lst


def correct_input_check() -> int:
    while True:
        player_input = input("Enter: 'row', 'column' where you want to place your sign: ")
        try:
            input_ = player_input.replace(' ', '')
            row, column = input_.split(',')
            row, column = int(row), int(column)

        except (ValueError, TypeError):
            print("Spatne zadani.")

        else:
            return row, column


def win_row(lst: list):
    for row in lst:
        string_row = ''
        for item in row:
            string_row += item
        if 'X|X|X|X|X|' in string_row:
            print("\nPlayer 'X' row won!.")
            quit()
        elif 'O|O|O|O|O|' in string_row:
            print("\nPlayer 'O' row won!")
            quit()
        else:
            continue


def win_column(lst: list):
    for i in range(1, len(lst)):
        string_column = ''
        for j in range(1, len(lst)):
            string_column += lst[j][i]
        if 'X|X|X|X|X|' in string_column:
            print("\nPlayer 'X' column won!.")
            quit()
        elif 'O|O|O|O|O|' in string_column:
            print("\nPlayer 'O' column won!")
            quit()
        else:
            continue


def win_diagonal(row: int, column: int, lst: list):
    string_add1 = ''
    string_reduce1 = ''
    string_add2 = ''
    string_reduce2 = ''
    for i in range(5):
        if (row + i) < len(lst) and (column + i) < len(lst):
            string_add1 += lst[row + i][column + i]
        if (row - i) > 0 and (column - i) > 0:
            string_reduce1 += lst[row - i][column - i]
        if (row + i) < len(lst) and (column - i) > 0:
            string_reduce2 += lst[row + i][column - i]
        if (row - i) > 0 and (column + i) < len(lst):
            string_add2 += lst[row - i][column + i]

    string_reduce1 = string_reduce1[::-1]
    string_reduce2 = string_reduce2[::-1]
    string_reduce_add = string_reduce1 + string_add1[1:]
    string_add_reduce = string_reduce2 + string_add2[1:]

    if 'X|X|X|X|X|' in string_reduce_add \
        or 'X|X|X|X|X|' in string_add_reduce:
        print("\nPlayer 'X' diagonal won!")
        quit()
    elif 'O|O|O|O|O|' in string_reduce_add \
        or 'O|O|O|O|O|' in string_add_reduce:
        print("\nPlayer 'O' diagonal won!")
        quit()


def board_print(list_board: list):
    lst = []
    for row in list_board:
        lst_temp = []
        for item in row:
            lst_temp.append(item)
        lst.append(' '.join(lst_temp))

    print('\n'.join(lst))



def tic_tac_toe(board_size: int):
    players = ["X", "O"]
    fill_game_board = game_board(board_size)
    board_print(fill_game_board)
    #pp(fill_game_board)

    #Defining size of board for input, once full board (i == max) -> game over
    for i in range((board_size - 1)**2):
        print(f"\n'{players[i%2]}' - player's turn.")

        #Correct input check, input within borders check:
        while True:
            row, column = correct_input_check()
            if row < board_size and column < board_size:
                # Check if chosen place is empty
                if fill_game_board[row][column] == '_|':
                    fill_game_board[row][column] = players[i % 2] + '|'
                    board_print(fill_game_board)
                    break
                else:
                    print("Already filled, try again.")
            else:
                pass


        #Row/Column/Diagonal win check
        win_row(fill_game_board)
        win_column(fill_game_board)
        win_diagonal(row, column, fill_game_board)


    else:
        print("Game board is full -> Game over.")
        quit()


tic_tac_toe(10)