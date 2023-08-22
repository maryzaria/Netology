import pytest
from ..main import summarize, get_list, get_dict, multiply


def test_multiply():
    x = 10
    y = 20
    res = multiply(x, y)
    expected = 200
    assert res == expected


def test_with_one_number():
    x = 20
    y = 22
    res = multiply(x)
    expected = 440
    assert res == expected


class TestMultiply():
    def test_something(self):
        x = 20
        y = 21
        res = multiply(x, y)
        expected = 400
        assert res > expected

    @pytest.mark.xfail
    def test_failure_pytest(self):
        x = 20
        y = -10
        res = summarize(x, y)
        expected = 30
        assert res == expected

    @pytest.mark.skipif(SOME_NUMBER > 25, reason='Too big value')
    def test_smth(self):
        x, y = 20, 21
        res = multiply(x, y)
        expected = 420
        assert res == expected


#параметризация
@pytest.mark.parametrize(
    'x,y,expected',
    [
        (20, 21, 420),
        (-10, 20, -200),
        (-10, -5, 50),
        (10, 11, 110),
        (-13, 21, -275)
    ]
)
def test_with_params(x, y, expected):
    res = multiply(x, y)
    assert res == expected