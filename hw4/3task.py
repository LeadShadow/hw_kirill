# Написати функцію! Є послідовність чисел - наприклад список,
# перевірити чи всі значення в ньому будуть унікальними(не повторюватись)
a_list = [1, 3, 3]
print(set(a_list))


def check_unique(list: list) -> str:
    if len(list) > len(set(list)):
        return 'Є неунікальні значення'
    elif len(list) == len(set(list)):
        return 'Все ок!'


print(check_unique([1, 3, 5, 7]))
