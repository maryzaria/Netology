import os


def cook_book(filename: str) -> dict:
    current = os.getcwd()
    full_path = os.path.join(current, filename)
    book = {}
    ingredient_keys = ['ingredient_name', 'quantity', 'measure']
    with open(full_path, 'rt', encoding='utf-8') as file:
        for line in file:
            dish = line.strip()
            count = int(file.readline())
            ingr = []
            for _ in range(int(count)):
                ingredients = file.readline()
                ingr.append(dict(zip(ingredient_keys, ingredients.strip().split(' | '))))
            book[dish] = ingr
            file.readline()
        return book


if __name__ == '__main__':
    print(cook_book('recipes.txt'))
