def main():
    dollars= dollars_to_float(input("How much was the meal? "))
    percent= percent_to_float(input("What percentage would you like to tip? "))
    tip= dollars * percent

    print(f"Leave {tip:2f}")


def dollars_to_float(d):
    if d[0] == "$":
        return float(d[1:])
    else:
        print("Amount in typed properly($##.##)")


def percent_to_float(p):
    if p[-1] == "%":
        return float(float(p[:-1]) / 100)
    else:
        print("Tip not typed in the right format(##%)")

main()