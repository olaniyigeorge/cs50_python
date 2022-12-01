def main():
    plate = input("Plate: ")
    
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")



def is_valid(s):
    condition_one(s)
    #print(condition_one(s))
    condition_two(s)
    #print(condition_two(s))
    condition_three(s)
    #print(condition_three(s))
    condition_four(s)
    #print(condition_four(s))

    
    return condition_one(s) and  condition_two(s) and condition_three(s) and condition_four(s)

#Check if first two characters are letters
def condition_one(s):
    lettersandnumbers=['A','B','C','D','E','F','G','H','I',
    'J','K','L','M','N','O','P','Q','R','S',
    'T','U','V','W','X','Y','Z',
    '0','1','2','3','4','5','6','7','8','9']
    if 2 <= len(s) <=6:
            if s[0].upper() and s[1].upper() in lettersandnumbers[:26]:
                    #print("Pass 1")
                    return True                    
            else:
                #print("Fail 1")
                return False
    else:
        #print("Fail 1--Pass len first")
        return False

#Check if len of plate is between 6 and 2
def condition_two(s):
    return  6 >= len(s) >= 2



#Check if the numbers are not in the middle 
def condition_three(s):
    lettersandnumbers=['A','B','C','D','E','F','G','H','I',
    'J','K','L','M','N','O','P','Q','R','S',
    'T','U','V','W','X','Y','Z',
    '0','1','2','3','4','5','6','7','8','9']

    if s[-1].upper() in lettersandnumbers[:26]:
        return False
    else:
        return True


#Check there are not spaces or punctuation marks
def condition_four(s):
    lettersandnumbers=['A','B','C','D','E','F','G','H','I',
    'J','K','L','M','N','O','P','Q','R','S',
    'T','U','V','W','X','Y','Z',
    '0','1','2','3','4','5','6','7','8','9']
    for letter in s:
        if letter.upper() not in lettersandnumbers:
            return False
    return True







main()



