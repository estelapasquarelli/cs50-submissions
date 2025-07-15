def main():
    dollars = dollars_to_float(input("How much was the meal? "))
    percent = percent_to_float(input("What percentage would you like to tip? "))
    tip = dollars * percent
    print(f"Leave ${tip:.2f}")


def dollars_to_float(d):
    dollar_without_symbol = float(d.removeprefix("$"))
    return dollar_without_symbol


def percent_to_float(p):
    percent_without_symbol = float(p.removesuffix("%"))
    return percent_without_symbol/100


main()
