
"""
SUDOKU check

Purpose of this script is to check, if numbers entered in sudoku 9 x 9 (3 times 3 x 3) are correct according to
Sudoku rules, or not.
"""


# Test Nums:
#       Yes:  295743861          No:  195743862
#             431865927               431865927
#             876192543               876192543
#             387459216               387459216
#             612387495               612387495
#             549216738               549216738
#             763524189               763524189
#             928671354               928671354
#             154938672               254938671


def main():
    # Creation of Sudoku board
    lst_sudoku = [''] * 9

    # Taking inputs in form: 1. row = 9 digits,..., 9. row
    # Entry input check, that it consists only from numbers and length is 9
    for i, _ in enumerate(lst_sudoku):
        try:
            item = int(input(f"{i + 1}: "))
            assert len(str(item)) == 9
        except ValueError:
            print('Not no.')
            quit()
        except AssertionError:
            print('Must be length 9')
            quit()
        else:
            lst_sudoku[i] = list(str(item))

    # Compliance with row - rule check; output: quit of script if rules are broken, otherwise None -> continue
    row_check(lst_sudoku)

    # Compliance with column - rule check; output: quit of script if rules are broken, otherwise None -> continue
    column_check(lst_sudoku)

    # Compliance of every 3 x 3 square - rule check; output: quit of script if rules are broken, otherwise None -> continue
    square_check(lst_sudoku)

    # If every rule comply, output of the script
    print('Yes')


# Row - rule check: every row consits of 9 different digits
def row_check(lst: list) -> None:
    for row in lst:
        if len(set(row)) != 9:
            print('No')
            quit()


# Column - rule check: every column consits of 9 different digits
def column_check(lst: list) -> None:
    # Two nested for loopes to extract 9 times a list. Check that everytime that list consists of 9 different digits,
    # then clear it and go for next list - column.
    #
    # Algorithm:
    #             value row 0 item 0, value row 1 item 0..., value row 8 item 0
    #             .
    #             .
    #             .
    #             value row 0 item 8, value row 1 item 8,..., value row 8 item 8

    for i in range(9):
        column_temp = set()
        for j in range(9):
            column_temp.add(lst[j][i])
        if len(column_temp) != 9:
            print('No')
            quit()
        else:
            column_temp.clear()


# Check 9 times of square 3 x 3
def square_check(lst: list) -> None:
    """
    There is need to check 9 times the square 3 x 3


    Algorithm flow:

                top left 3 x 3 square, top middle 3 x 3 square, top right 3 x 3 square
                middle left 3 x 3 square, middle middle 3 x 3 square, middle right 3 x 3 square
                bottom left 3 x 3 square, bottom middle 3 x 3 square, bottom right 3 x 3 square


                1st loop: value row 0 item 0, value row 0 item 1, value row 0 item 2
                          value row 1 item 0, value row 1 item 1, value row 1 item 2
                          value row 2 item 0, value row 2 item 1, value row 2 item 2


                2nd loop: Adding 3 to the item loop to move the the next 3 x 3square
                          value row 0 item 3, value row 0 item 4, value row 0 item 5
                          value row 1 item 3, value row 1 item 4, value row 1 item 5
                          value row 2 item 3, value row 2 item 4, value row 2 item 5
                .
                .
                .
                7th loop: Adding
                          value row 6 item 0, value row 6 item 1, value row 6 item 2
                          value row 7 item 0, value row 7 item 1, value row 7 item 2
                          value row 8 item 0, value row 8 item 1, value row 8 item 2
                .
                .
                .
                9th loop: value row 6 item 6, value row 6 item 7, value row 6 item 8
                          value row 7 item 6, value row 7 item 7, value row 7 item 8
                          value row 8 item 6, value row 8 item 7, value row 8 item 8

    """
    column_temp = set()
    for a in range(0, 7, 3):
        for b in range(0, 7, 3):
            for i in range(3):
                for j in range(3):
                    column_temp.add(lst[i + a][j + b])
            if len(column_temp) != 9:
                print('No')
                quit()
            else:
                column_temp.clear()


if __name__ == "__main__":
    main()
