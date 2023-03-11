from jar import Jar





def test_deposit():
    j = Jar(10)
    assert j.deposit(2) == 2
    j = Jar()
    assert j.deposit(3) == 3
    j = Jar(11)
    assert j.deposit(20) == None
    j = Jar(15)
    assert j.deposit(-1) == None


def test_capacity():
    j = Jar(10)
    assert j.capacity == 10
    j = Jar()
    assert j.capacity == 12
    j = Jar(11)
    assert j.capacity == 11
    j = Jar(-5)
    assert j.capacity == 15


def test_withdraw():
    j = Jar(10)
    j.deposit(6)
    assert j.withdraw(4) == 2

    j = Jar()
    j.deposit(4)
    assert j.withdraw(3) == 1

    j = Jar(11)
    j.deposit(5)
    assert j.withdraw(5) == 0

    j = Jar(15)
    j.deposit(6)
    assert j.withdraw(-3) == None
    


def test_size():
    j = Jar(10)
    j.deposit(3)
    assert j.size == 3

    j = Jar()
    j.deposit(4)
    j.withdraw(1)
    assert j.size == 3

    j = Jar(11)
    j.deposit(5)
    j.withdraw(2)
    assert j.size == 3

    j = Jar(15)
    j.deposit(6)
    j.withdraw(3)
    assert j.size == 3