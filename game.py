import random

def main():
    #Prompt for level
    level= get_int("Pick a level: ")
        
    #Randomly generate an integer between one and the level inclusive
    hidden_number = random.randint(1, level)

    #Process guess
    while True:
        #Make a guess
        guess= get_int("Make a guess: ")

        if guess < hidden_number:
            print("Too Small!")
        elif guess > hidden_number:
            print("Too Large!")
        else:
            print("Just Right!")
            break


def get_int(prompt):
    while True:
        try:
            i= int(input(prompt)) 
        except ValueError:
            pass
        else: #Check if the number is a positive number
            if i == abs(-i):
                return i
    


if __name__ == "__main__":
    main()