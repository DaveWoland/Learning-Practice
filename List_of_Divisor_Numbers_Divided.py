
def main():
    start = int(input("Start point: "))
    end = int(input("End point: "))
    divisor_start = int(input("Divisor start point: "))
    divisor_end = int(input("Divisor end point: "))

    lst_divisor_numbers = divisor_numbers(divisor_start, divisor_end)
    lst_numbers_divided = numbers_divided(start, end, lst_divisor_numbers)
    lst_divisor_no_divided = divisor_numbers_divided(lst_divisor_numbers, lst_numbers_divided)
    print()
    output_header(start, end)
    output_divisor_no_divided(lst_divisor_no_divided)



def divisor_numbers(start, end):
    lst_divisor_numbers = [number for number in range(start, end)]
    return lst_divisor_numbers

def numbers_divided(start, end, divisor):
    lst_numbers_divided = []
    for number in divisor:
        lst0 = []
        for x in range(start, end + 1):
            if x % number == 0:
                lst0.append(str(x))
        lst_numbers_divided.append(lst0)
    return lst_numbers_divided

def divisor_numbers_divided(lst_divisor, lst_no_divided):
    for i, number in enumerate(lst_divisor):
        lst_no_divided[i].insert(0, str(number))
        continue
    return lst_no_divided

def output_header(start, end):
    print(f"START POINT: {str(start)}\n"
          f"END POINT: {str(end)}\n"
          f"|{'Divisor':^9}|{'Numbers Divided':^28}|\n"
          f"{'=' * 40}")

def output_divisor_no_divided(lst):
    for row in lst:
        print(f"|{row[0]:^9}|{', '.join(row[1:]):^28}|")

main()