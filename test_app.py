from app import add_number

def test_add_number():
    assert add_number(2, 3) == 5
    assert add_number(0, 0) == 0
    assert add_number(-1, 1) == 0
    assert add_number(-5, -5) == -10
    assert add_number(2.5, 3.5) == 6.0