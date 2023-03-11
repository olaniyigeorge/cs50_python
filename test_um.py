from um import count


def test_words_containing_um():
    assert count("yummy") == 0
    assert count("I have a black umbrella.") == 0

    
def test_punctuation_marks_joined_to_it():
    assert count("I have a um, degree.") == 1
    assert count("Have we talked about the word um?") == 1
    

def test_combination():
    assert count("I couldn't find the um, black umbrella.")
    assert count("I thought I could um, study harder to  um, avoid repeating ums during my speech.") == 2

def test_cournercases():
    assert count("  I have a         um, degree.") == 1