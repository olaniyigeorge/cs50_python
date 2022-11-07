def main():
    emoticon= input("Type in an emoticon: ")
    print(f"Total converted '{convert(emoticon)}'")

def convert(e):
    happyface= e.replace(":)", "@")
    print(happyface)
    sadface= happyface.replace(":(", "#")
    print(sadface)
    return sadface





main()