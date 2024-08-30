import string
from itertools import product

import pytest

from main import count_words


@pytest.fixture
def fxt_large_word_list():

    # Generate a large word list by taking all combinations of 3 letters
    letters = string.ascii_lowercase
    return [''.join(p) for p in product("bcdefghijk", repeat=3)]


def test_more_of_same_item_occurences():
    """
        foo should not appear
    """
    res = count_words("bar baz foo foo zblah zblah zblah baz toto bar", 3)

    expected = [
        ("zblah", 3),
        ("bar", 2),
        ("baz", 2),
    ]

    assert len(res) == len(expected)

    for i in range(len(expected)):
        assert expected[i][0] == res[i][0]
        assert expected[i][1] == res[i][1]


def test_sorting(fxt_large_word_list):
    # TODO : Doesn't work , i need to debug the test but no time
    res = count_words(fxt_large_word_list, 3)

    assert res[0][0] < res[0][1]
    assert res[0][1] < res[0][2]


def test_not_enough_occurrences():
    res = count_words("bar baz", 3)

    expected = [
        ("bar", 1),
        ("baz", 1)
    ]

    assert len(res) == len(expected)

    for i in range(len(expected)):
        assert expected[i][0] == res[i][0]
        assert expected[i][1] == res[i][1]
