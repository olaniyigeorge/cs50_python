from twttr import shorten

#test lower and upper cases
def test_all_cases():
    assert shorten("TWITTER") == 'TWTTR'
    assert shorten("twitter") == 'twttr'

#test numbers
def test_numbers():
    assert shorten("CS50Python") == 'CS50Pythn'
    assert shorten("1234") == '1234'


#test spaces and other characters
def test_other_char():
    assert shorten("CS50_Python") == 'CS50_Pythn'
    assert shorten("Abeleje Olaniyi George") == 'blj lny Grg'