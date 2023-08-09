class FlatIterator:
    """Для вложенных списков вроде [[1, '2'], 3, [4, None]]"""
    def __init__(self, list_data: list) -> None:
        self.gen_data = self.flatten_list(list_data)

    def __iter__(self):
        return self

    @staticmethod
    def flatten_list(list_of_items: list) -> list:
        for item in list_of_items:
            if isinstance(item, list):
                yield from item
            else:
                yield item

    def __next__(self):
        return next(self.gen_data)


class FlatIteratorDeep:
    """Для списка любой степени вложенности"""
    def __init__(self, list_data: list) -> None:
        self.gen_data = self.flatten_list(list_data)

    def __iter__(self):
        return self

    def flatten_list(self, list_of_items: list) -> list:
        for item in list_of_items:
            if not isinstance(item, list):
                yield item
            else:
                yield from self.flatten_list(item)

    def __next__(self):
        return next(self.gen_data)


if __name__ == '__main__':
    d = [1, [2, 3], 'a', [10, None, 'aaaa'], [4], 5]
    print(*FlatIterator(d))
    data = [1, [2, 3, ['a', [10, None, 'aaaa'], 's'], 4], 5, [6, [7, 8, [9]], 10]]
    print(*FlatIteratorDeep(data))