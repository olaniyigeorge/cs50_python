greeting= input("Type in a greeting: ")


if greeting.strip()[0:5].lower() == 'hello':
    print("$0")
elif greeting.strip()[0].lower() == "h":
    print("$20")
else:
    print("$100")