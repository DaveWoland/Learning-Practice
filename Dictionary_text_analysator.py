text1 = """In the past, I have been manually keying in the financial data for stocks into Excel and then generate charts to visualize the data. This has taken up a lot of time and it’s very prone to human error.
Recently, I came to realize that Google Apps Script may be the rescue and possibly reduces all the manual work and thus automating the process of filling in financial data and generating charts."""

text2 = """The above shows the entry point that prompts dialog to accept user’s input and further validate the input before calling the API to retrieve the stock price quote. The first prompts for the stock code, followed by the time series (whether it’s 1-min, 5-min, 15-min, hourly or daily) and the number of data points. As the number of data points that will be returned can go up to thousands and this will result in very slow Google Sheet, we are adding this field with a warning to indicate that high number can cause slowness."""



def rozbor_vety(slovnik,text, poradi, znak):
    dct = {}
    lst = [slovo.strip(",.?!()") for slovo in text.split()]
    for slovo in lst:
        dct[f"text{poradi}"] = {
                                'Slova_pocet': sum(1 for slovo in lst if slovo.isalpha()),
                                f"Pocet_slov_na_{znak}": len(slova_na_pismeno(lst, znak)),
                                f"List_slov_na_{znak}": [slovo for slovo in lst if slovo.startswith(znak)],
                                f"Pocet_stejnych_slov": {slovo: lst.count(slovo) for slovo in sorted(lst)}
                                }
    slovnik.update(dct)
    return slovnik

def slova_na_pismeno(lst, pismeno):
    lst0 = [slovo for slovo in lst if slovo.startswith(pismeno)]
    return lst0

dct = {}
rozbor_vety(dct, text1, 1, 't')
rozbor_vety(dct, text2, 2, 'a')

print(dct)