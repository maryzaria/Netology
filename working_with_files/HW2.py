from HW1 import cook_book


def get_shop_list_by_dishes(dishes: list[str], person_count: int) -> dict:
    res = {}
    recipes = cook_book('recipes.txt')
    for dish in dishes:
        ingredients = recipes[dish]  # список ингридиентов
        for ingr in ingredients:
            ingredient_name, quantity, measure = ingr.values()
            if ingredient_name not in res:
                res[ingredient_name] = dict(zip(('measure', 'quantity'), (measure, int(quantity) * person_count)))
            else:
                res[ingredient_name]['quantity'] += int(quantity) * person_count
    return res


if __name__ == '__main__':
    print(get_shop_list_by_dishes(['Запеченный картофель', 'Омлет'], 2))
