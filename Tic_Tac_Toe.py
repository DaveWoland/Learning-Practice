
grid_empty = """
            +---+---+---+
            |   |   |   |
            +---+---+---+
            |   |   |   |
            +---+---+---+
            |   |   |   |
            +---+---+---+
"""

grid_inputs = """
            +---+---+---+
            | 1 | 2 | 3 |
            +---+---+---+
            | 4 | 5 | 6 |
            +---+---+---+
            | 7 | 8 | 9 |
            +---+---+---+
"""

#Výhra v řádku
def vyhra_radek(lst: list) -> bool:
    vysledek = False
    for i in range(0,7,3):
        if lst[i] == lst[i + 1] and lst[i] == lst[i + 2]:
            vysledek = True
    return vysledek

#Výhra v sloupci
def vyhra_sloupec(lst: list) -> bool:
    vysledek = False
    for i in range(3):
        if lst[i] == lst[i + 3] and lst[i] == lst[i + 6]:
            vysledek = True
    return vysledek

#Výhra diagonála
def vyhra_diagonala(lst: list) -> bool:
    a, b, c = 0, 4, 8
    x, y, z = 2, 4, 6
    vysledek = False
    if lst[a] == lst[b] and lst[a] == lst[c]:
        vysledek = True
    elif lst[x] == lst[y] and lst[x] == lst[z]:
        vysledek = True
    return vysledek


lst_cisla = [cislo for cislo in range(1, 10)]
znaky = ['O', 'X']
hra = 0
print(grid_empty)
while hra < 9:
    print(f"Player '{znaky[hra % 2]}'")
    vstup = input("Enter no: ")

    if vstup in grid_inputs:
        #Nahrazení čísla znakem v listu sloužícímu pro vyhodnocení výhry
        lst_cisla[int(vstup) - 1] = znaky[hra % 2]

        #Nahrazení čísla znakem O nebo X v gridu
        grid_inputs = grid_inputs.replace(vstup, znaky[hra % 2])

        #Grid pro výstup, kde se zobrazí pouze O a X
        grid_print = grid_inputs
        for i in range(10):
            grid_print = grid_print.replace(str(i), ' ')
        print(grid_print)

        #Zkontrolování výhry
        if vyhra_radek(lst_cisla):
            print(f"Won player '{znaky[hra % 2]}' row")
            break
        elif vyhra_sloupec(lst_cisla):
            print(f"Won player '{znaky[hra % 2]}' column")
            break
        elif vyhra_diagonala(lst_cisla):
            print(f"Won player '{znaky[hra % 2]}' diagonal")
            break


        hra += 1
    else:
        print("Wrong, input again.")

else:
    print("Draw")