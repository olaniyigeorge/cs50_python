import sys


def main():
    if len(sys.argv) < 2:
        sys.exit("Too few command-line arguments")
    if len(sys.argv) > 2:
        sys.exit("Too many command-line arguments")
    elif sys.argv[1][-3:].lower() != ".py":
        sys.exit("Not a Python file")

    name_of_file = sys.argv[1]

    line_count = 0
    try:
        with open(name_of_file, "r") as file:
            for line in file:
                # Skip blank lines
                if not line.strip():
                    continue
                # Skip line comments
                elif line.strip().lower().startswith("#"):
                    continue
                line_count += 1
                # print(line[:-1])
    except FileNotFoundError:
        sys.exit("File does not exit")

    print(line_count)


if __name__ == "__main__":
    main()
