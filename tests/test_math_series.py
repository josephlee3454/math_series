from math_series import __version__
from math_series.math_series import fibo_nth
from math_series.math_series import lucas_nth

def test_version():
    assert __version__ == '0.1.0'

def test_fib_nth_pass():
    actual = fibo_nth(1)
    expected = 1
    assert actual == expected
def test_fib_nth_fail():
    actual = fibo_nth(4)
    expected = 1
    assert actual != expected
def test_fib_nth_pass2():
    actual = fibo_nth(2)
    expected = 1
    assert actual == expected
def test_fib_nth_fail2():
    actual = fibo_nth(6)
    expected = 1
    assert actual != expected
def test_lucas_nth_pass():
    actual = lucas_nth(0)
    expected = 2
    assert actual == expected
def test_lucas_nth_fail():
    actual = lucas_nth(5)
    expected = 2
    assert actual != expected 
def test_lucas_nth_pass2():
    actual = lucas_nth(1)
    expected = 1
    assert actual == expected
def test_lucas_nth_fail2():
    actual = lucas_nth(6)
    expected = 1
    assert actual != expected
def test_lucas_nth_pass3():
    actual = lucas_nth(2)
    expected = 3
    assert actual == expected
def test_lucas_nth_fail3():
    actual = lucas_nth(9)
    expected = 3
    assert actual != expected
    