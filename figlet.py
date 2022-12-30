import sys
import pyfiglet
import random


def main():
    fonts=['standard', 'slant', 'rectangles', 'alphabet']
    #If len(argv) is 1, choose a random font form a list of fonts
    if len(sys.argv) == 1:
        text= get_text()
        #Choose randomly from a list of fonts
        random_font= random.choice(fonts)
        pyfiglet.print_figlet(text, font=random_font)    
    
    #If len(argv) is 3 in which case the second is either -f or '-font' 
    #...and the third is the name of a valid font, output text in the specified font
    elif len(sys.argv) == 3 and sys.argv[1].lower() in ['-f', '-font'] and sys.argv[2].lower() in fonts:
        text= get_text()
        #Print the text in the specified font
        pyfiglet.print_figlet(text, font=sys.argv[2])

    else:
        sys.exit("Invalid Usage")



def get_text():
    try:
        text= input("Type in the text: ")
    except:
        print("Type in some texts")
    else:
        return text




if __name__ == "__main__":
    main()