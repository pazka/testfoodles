from main import count_words


def test_main_example():
    res = count_words("bar baz foo foo zblah zblah zblah baz toto bar", 3)

    expected = [
        ("zblah", 3),
        ("bar", 2),
        ("baz", 2),
    ]
    
    assert len(res) == len(expected)

    for item, value,index in expected:
        assert item[0] == res[index][0]
        assert item[1] == res[index][1]
