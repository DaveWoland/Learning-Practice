
def display_convert(number = input("Enter no: ")) -> str:

    display_lst = [["###", "# #", "# #", "# #", "###"], ["  #", "  #", "  #", "  #", "  #"],
                   ["###", "  #", "###", "#  ", "###"], ["###", "  #", "###", "  #", "###"],
                   ["# #", "# #", "###", "  #", "  #"], ["###", "#  ", "###", "  #", "###"],
                   ["###", "#  ", "###", "# #", "###"], ["###", "  #", "  #", "  #", "  #"],
                   ["###", "# #", "###", "# #", "###"], ["###", "# #", "###", "  #", "###"]
                   ]


    str_no = str(number)

    for i in range(5):
        for c in str_no:
            try:
                int_no = int(c)
            except ValueError:
                print('Not a number!')
                quit()
            else:
                print(display_lst[int_no][i], end=' ')
        print()


if __name__ == "__main__":
    display_convert()
