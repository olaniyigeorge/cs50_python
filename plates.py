def main():
    my_plate= input("Type in a string of characters for your plate: ")
    print(is_valid(my_plate))


def is_valid(s):
    return condition_one(s) and  condition_two(s) and condition_three(s) and condition_four(s)




#Check if first two characters are letters
def condition_one(s):
    letters=['A','B','C','D','E','F','G','H','I',
    'J','K','L','M','N','O','P','Q','R','S',
    'T','U','V','W','X','Y','Z']

    s= s.strip()

    if 2 <= len(s) <=6:
        if s[0].upper() and s[1].upper() in letters:
                #print("Pass 1")
                return True                    
        else:
            #print("Fail 1")
            return False
    else:
        #print("Failed condition two")
        return False

#Check if len of plate is between 6 and 2
def condition_two(s):
    

    return  6 >= len(s.strip()) >= 2



#Check if the numbers are not in the middle 
def condition_three(s):
    letters=['A','B','C','D','E','F','G','H','I',
    'J','K','L','M','N','O','P','Q','R','S',
    'T','U','V','W','X','Y','Z']

    s = s.strip()

    try:
        int(s)
    except ValueError:
        pass
    else:
        return False


    for _ in s:
        try:
            int(_)
        except ValueError:
            continue
        else:
            if s[-1].upper() in letters:
                return False   
    
    return True
   


#Check if characters are either letters or numbers
def condition_four(s):
    lettersandnumbers=['A','B','C','D','E','F','G','H','I',
    'J','K','L','M','N','O','P','Q','R','S',
    'T','U','V','W','X','Y','Z',
    '0','1','2','3','4','5','6','7','8','9']
    s= s.strip()
    for letter in s:
        if letter.upper() not in lettersandnumbers:
            return False
    return True






if __name__ == "__main__":
    main()