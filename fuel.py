import sys


def main():
    question = input("Type in the question: ")

    # print(convert(question))

    print(guage(convert(question)))


def convert(fraction):
    operands = fraction.split("/")

    # Check if / is present is present in fraction
    if len(operands) == 1:
        return None
        # sys.exit("Question not in right format")

    x = fraction.split("/")[0]
    y = fraction.split("/")[-1]

    # Check if numerator and denominator are integers
    try:
        x = int(x)
        y = int(y)

    except ValueError:
        return None
        # sys.exit("ValueError")

    # Raise ZeroDivisionError if the denominator is zero
    if y == 0:
        return None
        # sys.exit("ZeroDivisionError")

    """ try:
        answer= x/y
    except ZeroDivisionError:
        raise ZeroDivisionError """

    # Check if x is greaer than Y
    if x > y:
        return None
        # sys.exit("ValueError")

    answer = x / y
    return int(answer * 100)


def guage(percentage):
    try:
        int(percentage)
    except TypeError:
        return "Input not right"

    if int(percentage) in range(0, 101):
        if percentage <= 1:
            return "E"
        elif percentage >= 99:
            return "F"
        else:
            return f"{percentage}%"
    else:
        # print("Percentage not right")
        return "Percentage not right"


if __name__ == "__main__":
    main()
