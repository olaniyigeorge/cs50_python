from plates import condition_one, condition_two, condition_three, condition_four


#Test that the first two characters are letters
def test_condition_one():
    assert condition_one("cs50") == True
    assert condition_one("c s50") == False
    assert condition_one(" cs50") == True



#Test to see if len of plate is between 6 and 2
def test_condition_two():
    assert condition_two("c") == False
    assert condition_two("cs") == True
    assert condition_two("cs50") == True
    assert condition_two("abcde") == True
    assert condition_two("abcdef") == True
    assert condition_two("abcdefg") == False
    assert condition_two("") == False
    assert condition_two("      ") == False


#Test to see if numbers are not in the middle 
def test_condition_three():
    assert condition_three("cs50p") == False
    assert condition_three("cs50") == True
    assert condition_three("50") == False
    assert condition_three("50cs") == False


#Test if characters are either letters or numbers
def test_condition_four():
    assert condition_four("CS") == True
    assert condition_four("CS50") == True
    assert condition_four("CS_50") == False
    assert condition_four("cs 50") == False