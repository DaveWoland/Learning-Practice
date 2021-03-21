
horizont_hist = ([4,5,7,10,6,3,2])

def vert_histogram(data: list) -> None:
    top_row = max(data)

    lst_histogram = []
    for i in range(max(data)):
        lst_temp = []
        for item in data:
            if item >= (top_row - i):
                lst_temp.append('**')
            else:
                lst_temp.append('  ')

        lst_histogram.append(' '.join(lst_temp))

    for i in range(max(data)):
        print(f"{max(data) - i:>3}| {lst_histogram[i]}")

    print(f"  {'-' * (len(data) + 1) * 3}")

vert_histogram(horizont_hist)