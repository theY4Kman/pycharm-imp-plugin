import pytest
from pytest_lambda import static_fixture, lambda_fixture

my_toplevel_static_fixture = static_fixture(123)


@pytest.fixture
def caret(my_toplevel_static_fixture):
    return 20


@pytest.mark.parametrize('v', [
    pytest.param(1),
])
def test_stuff(v):
    a = v


a = lambda_fixture(lambda : 123)

class TestStuff:
    caret = lambda_fixture('caret')
    
    def test_it(self, caret, my_toplevel_static_fixture):
        assert caret
        a = caret
        b = my_toplevel_static_fixture


l = [1, 2.0, 'c']

for o in l:
    print(o)


from pytest_lambda import lambda_fixture

renaming = lambda_fixture(lambda: None)


class TestStuff:
    renaming = lambda_fixture('renaming')

    def test_it(self, renaming):
        assert renaming


alpha = 24

class Things:
    alpha = 12