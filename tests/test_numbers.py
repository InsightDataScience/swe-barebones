from swe_barebones.numbers import Numbers
import pytest
"""
This script tests methods in a number theory class called Numbers
"""

test_perfect_number_data = [(6,True),(28,True),(496,True),(8,False)]
@pytest.mark.parametrize('x,expected',test_perfect_number_data)
def test_perfect_number(x,expected):
    num = Numbers()
    assert num.perfect_number(x) == expected

perfect_numbers = [6,28,496,8128,33550336]
def test_perfect_number_large_p():
    num = Numbers()
    for x in range(2,1000):
        if x in perfect_numbers:
            assert num.perfect_number(x) == True
        else:
            assert num.perfect_number(x) == False
