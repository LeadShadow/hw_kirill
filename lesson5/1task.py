# Мы разрабатываем кулинарный блог. И в рецептах, при написании списка ингредиентов,
# мы разделяем их запятыми, а перед последним ставим союз "і", как в примере ниже:

# 2 eggs, 1 liter sugar, 1 tsp salt and vinegar

# Напишите функцию format_ingredients, которая будет принимать на вход список из ингредиентов
# ["2 eggs", "1 liter sugar", "1 tsp salt", "vinegar"] и возвращать собранную строку
# из его элементов в описанный выше способ. Ваша функция должна уметь обрабатывать списки
# любой длины.
def format_ingredients(items):
    new = ''
    for s in items[:-2]:
        new += s + ', '
    return new + items[-2] + ' і ' + items[-1]


items = ["2 eggs", "1 liter sugar", "1 tsp salt", "vinegar", 'lemon']
print(format_ingredients(items))
