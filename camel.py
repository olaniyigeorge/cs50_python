camelcase= input("Name in camel case: ")

snakecase= ""
for  letter in camelcase:
    if letter == letter.upper():
        snakecase = snakecase + "_"
    snakecase = snakecase + f"{letter.lower()}"


print(snakecase)
