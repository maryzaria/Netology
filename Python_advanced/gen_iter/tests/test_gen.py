import types

from ..generators import flat_generator, flat_generator_deep


def test_gen_1():
    data = [['a', 'b', 'c'], [1, 2, None], ['d', 10, 'e']]
    result = ['a', 'b', 'c', 1, 2, None, 'd', 10, 'e']
    for flat_item, check_item in zip(flat_generator(data), result):
        assert flat_item == check_item
    assert list(flat_generator(data)) == result
    assert isinstance(flat_generator(data), types.GeneratorType)


def test_gen_2():
    list_of_lists_2 = [
        [['a'], ['b', 'c']],
        ['d', 'e', [['f'], 'h'], False],
        [1, 2, None, [[[[['!']]]]], []]
    ]

    for flat_iterator_item, check_item in zip(
            flat_generator_deep(list_of_lists_2),
            ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None, '!']
    ):
        assert flat_iterator_item == check_item

    assert list(flat_generator_deep(list_of_lists_2)) == ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None, '!']

    assert isinstance(flat_generator_deep(list_of_lists_2), types.GeneratorType)

