# Как мы уже знаем, ключ в словаре должен быть уникальным, а вот значение его нет.
# Реализуйте функцию lookup_key для поиска всех ключей по значению в словаре.
# Первым параметром в функцию мы передаем словарь, а вторым — значение, которое хотим найти.
# Таким образом результат может быть как список ключей, так и пустой список,
# если мы ничего не найдем.

data = [
    {
    'name': 'Bill',
    'surname': 'Samus',
    'age': 20
},
    {
        'name': 'Bill',
        'surname': 'Samus',
        'age': 20
    }
]
print(data['name'])


def lookup_key(data, value):
    list_1 = []
    for k in data:
        if data[k] == value:
            list_1.append(k)
    return list_1


if __name__ == "__main__":
    print(lookup_key(data, 'Samus'))
