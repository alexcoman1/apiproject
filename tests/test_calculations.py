from calculations import add, subtract, multiply, divide

def test_add():
    print("testing add")
    sum = add(5, 3)
    assert sum == 8

def test_subtract():
    assert subtract(9, 4) == 5

def test_multiply():
    assert multiply(3, 3) == 9

def test_divide():
    assert divide(9, 3) == 3