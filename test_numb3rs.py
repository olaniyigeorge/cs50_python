from numb3rs import validate


def test_ipv4_range():
    assert validate('0.0.0.0') == True
    assert validate('1.1.1.1') == True
    assert validate('2.22.255.0') == True
    assert validate('255.255.255.255') == True
    
    
    
    assert validate('512.512.512.512') == False
    assert validate('1.2.3.1000') == False
    
    assert validate("1.0.275.20") == False
    assert validate('27.0.0.800') == False
    

    
def test_ipv4_string():
    assert validate('O.la.ni.yi') == False
    assert validate("20.G.23.255") == False
    assert validate('2o.34.55.2') == False
    assert validate('George') == False
    

def test_ipv4_corner_cases():
    assert validate('2. .24.25') == False
    assert validate('1..24.254') == False
    assert validate('') == False
    assert validate('0.00.0.000') == True

    assert validate('27.0.0.0') == True
    assert validate('27.0.2.1') == True