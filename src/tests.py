import pytest

from db import db_things
from client import search_things


@pytest.mark.parametrize("test_input,expected", [(("trousers", 1, 45), 2),
                                                 (("trousers", 30, 45), 1),
                                                 (("trousers", 45, 45), 1),
                                                 (("trousers", 46, 45), 0),
                                                 (("trosers", 1, 45), 0),
                                                 (("trouser", 1, 45), 6),
                                                 (("hat", 1, 45), 0),
                                                 (("hat", 1, 1000), 20),
                                                 (("hats", 1, 1000), 10)])
def test_eval(test_input, expected):
    assert search_things(test_input) == expected
