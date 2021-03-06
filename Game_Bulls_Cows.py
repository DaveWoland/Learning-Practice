
from random import sample
from time import time

def main():
    start = time()

    text0 = "I've generated a random 4 digits number for you."
    text1 = "Let's play a bulls and cows game."

    print(f"Hi there!\n"
          f"{'-'*len(text0)}\n"
          f"{text0}\n"
          f"{text1}\n"
          f"{'-'*len(text0)}")

    guess_count = 0

    #Vygenerovani 4 cislic
    lst_4 = random_4()

    #Vyhodnoceni tipu uzivatele
    tipovani = True
    while tipovani:
        guess_count += 1
        # Vstup a kontrola vstupu uzivatele
        player_input_string = vstup_kontrola()


        #Prevod vstupu uzivatele na list cisel
        player_input_lst = vstup_prevod(player_input_string)

        #Kontrola, zda již neuhodl správně 4-číslí
        if player_input_lst == lst_4:
            print(f"Correct, you've guessed the right number.")
            break
        else:
            #Kontrola shody čísel a umístění
            bull_cow(player_input_lst, lst_4)

        oddelovac(text0)


    end = time() - start

    #Čas hry převedený do formátu mm : ss
    game_time = game_time_format(end)
    print(f"You had {guess_count} {['guess', 'guesses'][guess_count != 1]}.")
    print(f"Your game took: {game_time}")

def oddelovac(text: str) -> str:
    print(len(text) * "-")


#def fce generovani 4 cisel (zadne se neopakuje, prvni nesmi byt 0)
def random_4() -> list:
    check = True
    #generuje 4-cisly (kazde cislo jine), dokud neplati podminka, ze 1. cislo se nerovna 0
    while check:
        lst = [cislo for cislo in sample(range(10), 4)]
        if lst[0] != 0:
            break
    return lst


#def fce vstup a kontrola hracem zadaneho cisla, ze je presne 4 znaky, znaky jsou cisla a prvni neni 0
def vstup_kontrola() -> str:
    kontrola = True
    while kontrola:
        player_input = input("Enter a number: ")
        if len(player_input) != 4 or player_input[0] == '0' or not player_input.isdigit() or len(set(player_input)) != 4:
            print("Wrong input! Try again.")
            continue
        else:
            kontrola = False

    return player_input

#def fce prevedeni uzivatelova vstupu (stringu) na list cisel
def vstup_prevod(string: str) -> list:
    lst_vstup = [int(char) for char in string]
    return lst_vstup

#def fce kontrola shody cisel a umisteni, kontrola poctu spravnych cisel
def bull_cow(player: list, game_no: list) -> str:
    spravna_pozice = 0
    spravne_cislo = 0
    byk, krava = ['bulls', 'bull'], ['cows', 'cow']

    for i, x in enumerate(player):
        for j, y in enumerate(game_no):
            if x == y and i == j:
                spravna_pozice += 1
                break
            elif x == y:
                spravne_cislo += 1
                break

    vystup = [f"{spravna_pozice} {byk[spravna_pozice == 1]}, {spravne_cislo} {krava[spravne_cislo == 1]}"]
    print(vystup)

#def fce pro převod času hry do formátu mm : ss
def game_time_format(time) -> str:
    output = f"{int(time // 60)} min : {(time % 60):.0f} sec"
    return output


main()



