def main():
    word= input("Type in a word: ")
    print(shorten(word))



def shorten(word):
    abbr= ""
    for _ in word:
        if _.lower() not in ['a', 'e', 'i', 'o', 'u']:
            abbr += _
            
    
    return abbr



if __name__ == "__main__":
    main()
