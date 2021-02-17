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

#Projde list a sečte v něm všechna čísla, včetně listů v listu
def soucet_listu(sekvence):
    soucet = 0
    for prvek in sekvence:
        if type(prvek) == int:
            soucet += prvek
        elif type(prvek) == bool:
            continue
        elif type(prvek) == str:
            soucet += soucet_cisel_v_stringu(prvek)
        elif type(prvek) == list:
            soucet += soucet_listu(prvek)
        elif type(prvek) == tuple:
            soucet += soucet_listu(prvek)
    return soucet

