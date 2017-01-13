from swe_barebones.dummy import Dummy
import pytest

def test_blah():
    assert 1 != 1

def test_simple_addition():
    d = Dummy(data=[1,2,3])
    assert d.addition(1,1) == 2

addition_testdata = [(1,1,2),(2,2,4),(-1,-1,-2),(None,1,1)]

@pytest.mark.parametrize('x,y,expected',addition_testdata)
def test_parametrized_addition(x,y,expected):
    d = Dummy(data=[1,2,3])
    assert d.addition(x,y,) == expected 
