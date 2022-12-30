import random

def main():
    score= 0

    level= get_level()

    number_of_questions= 10
    #For 10 questions
    for _ in range(number_of_questions):
        #Initiate each question with 0trials and generate x and y
        trial = 0
        x= generate_integer(level)
        y= generate_integer(level)
        answer =  x + y

        while trial < 3:
            #For each trial, ask the question
            print(f"{x} + {y} = ", end="")
            your_answer= int(input())

            #If answer is correct add to the score and break to the next question
            if your_answer == answer:
                score= score + 1
                break
            #If answer is wrong, print EEE and move to the next trial for that question    
            
            #Display the correct answer after 3 trials
            elif trial == 3:
                print(f"{x} + {y} = {answer}")
                break
            else:
                #Display EEE and reprompt the user with the same question if anwser is wrong
                print("EEE")
                trial+=1
    
    #Output the user's score. A number out of total number of questions            
    print(f"Your score is {score} out of {number_of_questions}.")


#Get level
def get_level():
    try:
        while True:
            #Prompt for a a level l and Reprompt if n isn't 1,2 or 3
            l= int(input("Type in the level: "))
            if l not in [1,2,3]:
                continue
            else:
                break
    except ValueError:
        print("Not an integer")
    
    return l

#Generate integer
def generate_integer(level):
    return random.randint((10**(level-1)), (10**(level)))




if __name__ == "__main__":
    main()

