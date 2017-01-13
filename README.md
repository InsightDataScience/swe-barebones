# swe-barebones

#Introduction

This is a barebones framework to understand how a repo should be set up

# How to get it

git clone https://github.com/InsightDataScience/swe-barebones.git

pip3 install -r -U requirements.txt

# Run it

jupyter notebook Barebones.ipynb

Run through the cells and make sure everything works (tough!)

# Run tests

From the top level directory, run:

py.test

You should see something like:

======================================= test session starts ========================================
platform darwin -- Python 3.5.2, pytest-3.0.5, py-1.4.32, pluggy-0.4.0
rootdir: /Users/BenRegner/dev/insight/swe-barebones, inifile:
collected 6 items

tests/test_dummy.py F....F

============================================= FAILURES =============================================
____________________________________________ test_blah _____________________________________________

    def test_blah():
>       assert 1 != 1
E       assert 1 != 1

tests/test_dummy.py:5: AssertionError
_______________________________ test_parametrized_addition[None-1-1] _______________________________

x = None, y = 1, expected = 1

    @pytest.mark.parametrize('x,y,expected',addition_testdata)
    def test_parametrized_addition(x,y,expected):
        d = Dummy(data=[1,2,3])
>       assert d.addition(x,y,) == expected

tests/test_dummy.py:16:
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _

self = <swe_barebones.dummy.Dummy object at 0x11200f7b8>, x = None, y = 1

    def addition(self,x,y):
>       return x+y
E       TypeError: unsupported operand type(s) for +: 'NoneType' and 'int'

swe_barebones/dummy.py:10: TypeError
================================ 2 failed, 4 passed in 3.33 seconds ================================

# Go Develop

Please ask us if you have any questions about why things are set up the way they are, if it seems dumb, try to think of why it might be that way.

