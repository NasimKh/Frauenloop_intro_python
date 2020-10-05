#test_nearest_num.py
# Create a test file and start the name with test_
from nearest_num import nearest_square


# Define unit test functions that start with test_ inside the test file


def test_nearest_square_5():
    assert (nearest_square(5)==4)


def test_nearest_square_9():
    assert(nearest_square(9) == 10)

def test_nearest_square_n10():
    assert(nearest_square(-10)== 0)


def test_nearest_square_0():
    assert(nearest_square(0) == 0)

