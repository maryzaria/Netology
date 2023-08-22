def summarize(x: int, y: int) -> int:
    return x + y


def multiply(x: int, y: int) -> int:
    return x * y


def get_dict():
    return {'name': 'Ivan', 'age': 29, 'city': 'Moscow'}


def get_list():
    return [1, 2, 3, 4]

#1
# res = summarize(10, 20)
# expected = 30
# expected2 = 35
#
# assert res == expected2

#2
# res = multiply(10, 20)
# expected = 1000
# assert res < expected

#3

# dict1 = get_dict()
# key1 = 'name'
# key2 = 'surname'
# assert key1 in dict1
# assert key2 in dict1

#операции сравнения ==, !=, >, <, >=, <=
#проверка на вхождение in, not in
#проверка is, is not
# isinstance(), issubclass()
