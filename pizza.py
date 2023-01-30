import sys
from tabulate import tabulate
import csv


def main():
    if len(sys.argv) < 2:
        sys.exit("Too few command-line arguments")
    if len(sys.argv) > 2:
        sys.exit("Too many command-line arguments")
    elif sys.argv[1][-3:].lower() != ".py":
        sys.exit("Not a CSV file")

    filename = sys.argv[1]
    try:
        with open(filename, "r") as file:
            reader = csv.reader(file)
            rows = []
            for row in reader:
                rows.append(row)
    except FileNotFoundError:
        sys.exit("File not found.")

    print(tabulate(rows, headers="firstrow", tablefmt="grid"))


if __name__ == "__main__":
    main()
