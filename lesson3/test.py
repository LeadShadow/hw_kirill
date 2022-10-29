a = 10
b = 20


def hello(x, y):
    x = 200
    y = 200
    # global a, b
    # a = 200
    # b = 200
    return x, y


hello(x=a, y=b)  # None
print(a, b)
# аргументи - в функції
# параметри те шо ми передаємо в функцію


def plus(a, b):
    return a + b


result = plus(a, b)
print(result)


def t(a=5, *num, **book):
    print('a =', a)
    for i in num:
        print('i =', i)
    for k, v in book.items():
        print(k, v)


print(t(10, 1, 2, 3, 'sasha', Jack=1000, Sasha=2000, Misha=3000))


