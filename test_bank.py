from bank import value

def test_greeting_with_leading_spaces():
    assert value(" Hey Man ") == 20
    assert value(" Hello Etta") == 0
    assert value(" ") == 100
    assert value("  Bruh") == 100


def test_hello_in_diff_cases():
    assert value("Hello, brother") == 0
    assert value("hello, Odunayo") == 0

def test_words_starting_with_h():
    assert value("hey brother") == 20
    assert value("How are you?") == 20

