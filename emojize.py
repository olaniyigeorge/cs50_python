import emoji

def main():
    #get input
    text= input("Type in a text containg emojis...: ")

    #compare it a list of all test data
    print("Output: ", end="")
    print(emoji.emojize(text, language='alias'))



if __name__ == "__main__":
    main()