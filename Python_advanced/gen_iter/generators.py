def flat_generator(data: list) -> list:
    for item in data:
        if isinstance(item, list):
            yield from item
        else:
            yield item


def flat_generator_deep(data: list) -> list:
    """Для списка любой степени вложенности"""
    for item in data:
        if not isinstance(item, list):
            yield item
        else:
            yield from flat_generator_deep(item)


if __name__ == '__main__':
    d = [1, [2, 3], 'a', [10, None, 'aaaa'], [4], 5]
    print(*flat_generator(d))
    data = [1, [2, 3, ['a', 's'], 4], 5, [6, [7, 8, [9]], 10]]
    print(*flat_generator_deep(data))

