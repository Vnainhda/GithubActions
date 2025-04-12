from src.math_operations import add,subtract

def test_add():
    assert add(2,3) == 5
    assert add(4,-1) == 3

def test_subtract():
    assert subtract(5,3) == 2
    assert subtract(4,2) == 2
    assert subtract(8,5) == 3