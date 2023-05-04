import os


def cook_book(filename: str) -> dict:
    current = os.getcwd()
    full_path = os.path.join(current, filename)
    book = {}
    ingredient_keys = ['ingredient_name', 'quantity', 'measure']
    with open(full_path, 'r', encoding='utf-8') as file:
        for line in file.read().split('\n\n'):
            dish, count, *ingredients = line.split('\n')
            for ingr in ingredients:
                book.setdefault(dish, []).append(dict(zip(ingredient_keys, ingr.split(' | '))))
        return book


if __name__ == '__main__':
    print(cook_book('recipes.txt'))
