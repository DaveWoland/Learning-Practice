TEXTS = ['''
Situated about 10 miles west of Kemmerer, 
Fossil Butte is a ruggedly impressive 
topographic feature that rises sharply 
some 1000 feet above Twin Creek Valley 
to an elevation of more than 7500 feet 
above sea level. The butte is located just 
north of US 30N and the Union Pacific Railroad, 
which traverse the valley. ''',

'''At the base of Fossil Butte are the bright 
red, purple, yellow and gray beds of the Wasatch 
Formation. Eroded portions of these horizontal 
beds slope gradually upward from the valley floor 
and steepen abruptly. Overlying them and extending 
to the top of the butte are the much steeper 
buff-to-white beds of the Green River Formation, 
which are about 300 feet thick.''',

'''The monument contains 8198 acres and protects 
a portion of the largest deposit of freshwater fish 
fossils in the world. The richest fossil fish deposits 
are found in multiple limestone layers, which lie some 
100 feet below the top of the butte. The fossils 
represent several varieties of perch, as well as 
other freshwater genera and herring similar to those 
in modern oceans. Other fish such as paddlefish, 
garpike and stingray are also present.'''
         ]

# registrovani uzivatele
registered_users = {'bob': '123', 'ann': 'pass123', 'mike': 'password123', 'liz': 'pass123'}

user = input("Username: ")
password = input("Password: ")

line = "-" * 40

word_count = 0
word_title_count = 0
word_upper_count = 0
word_lower_count= 0
numbers_count = 0
numbers_sum = 0

if registered_users.get(user) == password:
    print(line)
    print(f"Welcome to the app, {user}.\n"
          f"We have {str(len(TEXTS))} texts to be analyzed.")
    print(line)

    choose = input(f"Enter a number btw. 1 and {str(len(TEXTS))} to select: ")
    if not choose.isdigit() or int(choose) not in range(1,len(TEXTS) + 1):
        print("Wrong input!")
        exit()
    selected_text = int(choose) - 1
    print(line)

    #Výpočet všech hodnot
    text_split = TEXTS[selected_text].split()
    clean_text = []
    clean_text = [prvek.strip(".,?!'") for prvek in text_split]

    word_count = len(clean_text)

    for prvek in clean_text:
        if prvek.istitle():
            word_title_count += 1
        elif prvek.islower():
            word_lower_count += 1
        elif prvek.isupper():
            word_upper_count += 1
        elif prvek.isdigit():
            numbers_count += 1
            numbers_sum += int(prvek)

    print(f"There are {word_count} words in the selected text.\n"
          f"There are {word_title_count} titlecase words.\n"
          f"There are {word_upper_count} uppercase words.\n"
          f"There are {word_lower_count} lowercase words.\n"
          f"There are {numbers_count} numeric strings.\n"
          f"The sum of all the numbers {numbers_sum}.")
    print(line)

    #Stanovení délky listu pro počet indexů (př. index 5: pětipísmenná slova)
    longest_word = 0
    for prvek in clean_text:
        if prvek.isdigit():
            continue
        else:
            if len(prvek) > longest_word:
                longest_word = len(prvek)

    word_lenght = [0] * (longest_word + 1)

    #Přižazení slova na index odpovídající jeho délce
    for prvek in clean_text:
        if prvek.isdigit():
            continue
        else:
            word_lenght[len(prvek)] += 1

    print("LEN|  OCCURENCES  |NR.")
    print(line)
    for i, prvek in enumerate(word_lenght):
        if not i or not prvek:
            continue
        else:
            print(f"{str(i):>3}|{'*'*prvek}{' '*(max(word_lenght) - (prvek - 1))}|{str(prvek)}")

    print("\nHave a nice day.")

else:
    print(f"Wrong user/password!")
    exit()

