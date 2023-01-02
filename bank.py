def main():
    greeting= input("Type in a greeting: ")
    print(value(greeting))


def value(greeting):
    greeting = greeting.strip()
    if greeting and greeting[0:5].lower() == 'hello':
        return 0
    elif greeting and greeting[0].lower() == 'h':
        return 20
    else:
        return 100

if __name__ == "__main__":
    main()