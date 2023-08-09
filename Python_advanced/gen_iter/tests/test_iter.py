from ..iterators import FlatIterator, FlatIteratorDeep


def test_iter_1():
    d = [1, [2, 3], 'a', [10, None, 'aaaa'], [4], 5]
    result = [1, 2, 3, 'a', 10, None, 'aaaa', 4, 5]
    for flat_item, check_item in zip(FlatIterator(d), result):
        assert flat_item == check_item
    assert list(FlatIterator(d)) == result


def test_iter_2():
    d = [1, [2, 3, ['a', [10, None, 'aaaa'], 's'], 4], 5, [6, [7, 8, [9]], 10]]
    result = [1, 2, 3, 'a', 10, None, 'aaaa', 's', 4, 5, 6, 7, 8, 9, 10]
    for flat_item, check_item in zip(FlatIteratorDeep(d), result):
        assert flat_item == check_item
    assert list(FlatIteratorDeep(d)) == result
