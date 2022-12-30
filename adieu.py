names= []

while True:
    try:
        name= input("Input a name: ")
    except KeyboardInterrupt:
        print()
        break
    else:
        if len(name) < 1: #if not name
            continue
        else:
            names.append(name.title())

print(f"Adieu, adieu, to", end="")

if len(names) > 2:
    for _ in names[:-1]:
        print(f" {_},", end="")
    print(f" and {names[-1]}")
elif len(names) == 2:
        print(f" {names[0]} and {names[-1]}")
elif len(names) == 1:
    print(f" {names[-1]}")

