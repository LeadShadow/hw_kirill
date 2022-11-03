# Мы проводим розыгрыш призов среди первых 50 подписчиков ютуб-канала.
# У нас есть 7 призов для розыгрыша. Может возникнуть вопрос, сколько различных
# списков победителей мы можем получить при розыгрыше?
# Для этого мы будем использовать формулу сочетаний без повторений

# Cnk = n! / ((n - k)! · k!)

# где n — это общее количество людей (случаев), а k — количество людей, получивших призы.

# Напишите функцию number_of_groups, которая принимает параметры n и k, и с
# помощью функции factorial возвращает нам, сколько различных списков победителей
# мы можем получить при розыгрыше

# Примечание: Обратите внимание, какие большие значения мы получаем для факториала.
# Рекурсивные выражения надо всегда применять с осторожностью при вычислениях,
# чтобы не получить переполнение.

def factorial(n):
    if n <= 1:
        return 1
    else:
        return n * factorial(n - 1)


def number_of_groups(n, k):
    return factorial(n) // (factorial(n-k) * factorial(k))


# factorial(n) -> 5! -> 120
# factorial(n-k) -> 3! -> 6
# factorial(k) -> 2! -> 2

if __name__ == "__main__":
    print(number_of_groups(5, 2))
