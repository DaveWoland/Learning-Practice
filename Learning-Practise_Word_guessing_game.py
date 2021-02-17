import random

text = """
        Monica Anna Maria Bellucci is an Italian actress and model. 
        She began her career as a fashion model, modelling for Dolce & Gabbana
        and Dior, before making a transition to Italian films and later
        American films and French films.
        """

def main(text, guess = 10):
    pc_choice = random.choice(words_to_chose_from(text))
    seeking_word_lst = ["_"]*len(pc_choice)

    print("I'm thinking of a word. What word is it?")
    print(' '.join(seeking_word_lst))
    while guess:
        user_guess = input(f"Guess a letter ({guess} guesses available): ")
        if user_guess in pc_choice:
            seeking_word_lst = replace_letters(seeking_word_lst, user_guess, pc_choice)
            char_count = letters_count(user_guess, pc_choice)
            print(f"Yes, there {['is 1 letter', 'are '+str(char_count)+' letters'][bool(char_count - 1)]} '{user_guess}'")
            print(' '.join(seeking_word_lst))
            if pc_choice == (''.join(seeking_word_lst)):
                result = "You won!"
                break
        else:
            print(f"No the letter '{user_guess}' is not in my word")
            guess -= 1
    else:
        result = "You lost!"

    print(result)
    return result


def words_to_chose_from(text):
    lst0 = [slovo.strip(",.?!") for slovo in text.split()]
    lst_words = [slovo for slovo in lst0 if slovo.isalpha()]
    return lst_words

def replace_letters(lst, letter, _string):
    for i, char in enumerate(_string):
        if letter == char:
            lst[i] = char
    return lst

def letters_count(letter, word):
    x = word.count(letter)
    return x

main(text, guess=2)