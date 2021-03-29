
dct = {'a1':{'a11':"a11_output", 'a12':{'a121':'a121_output'}, 'a13':'a13_output'}, 'a2':'a2_output', 'a3':{'a31':'a31_output', 'a32':'a32_output'}}

def main(dct_main: dict, key_main: str) -> str:
    """
    Function 'main' has purpose of enclosing frame, to get a value from inside function 'test'.
    Variable 'output' has purpose of local variable of function 'main', to prevent possible
    misstakes of dynamic variable changes, if the variable ('ouput') would be in global framework.

    """

    output = ''

    #Function 'test' doesn't return any value, it recursively goes through the whole dictionary.
    #At the moment it finds searched value 'searched_key' correlated to 'key_main', it store this value
    #inside the variable 'output'.

    #Variable 'output' is in function 'test' declared as 'nonlocal', so I could evoke it's value
    #from the function 'test' and not loose it during continuous itteration through the dicctionary.

    def test(dct_: dict, searched_key: str) -> None:
        for key, value in dct_.items():
            if key == searched_key:
                nonlocal output
                output = value
            else:
                if isinstance(value, dict):
                    test(value, searched_key)

    #Running function 'test' to evoke value of 'output'.
    test(dct_main, key_main)

    return output

print(main(dct, 'a13'))