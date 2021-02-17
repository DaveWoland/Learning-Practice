#Sečte čísla ve stringu jako celky, ne každé zvlášť
def soucet_cisel_v_stringu(string):
    cisla = ''
    list_cisel = []
    for i, znak in enumerate(string):
        if znak.isdigit():
            cisla += znak
            if i == len(string) - 1:
                list_cisel.append(int(cisla))
        else:
            if not cisla:
                continue
            else:
                list_cisel.append(int(cisla))
                cisla = ''
    return sum(list_cisel)








