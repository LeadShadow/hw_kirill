# №1

def get_fullname(first_name, last_name, middle_name=None):
    return f'{first_name} {middle_name} {last_name}' if middle_name else f'{first_name} {last_name}'


# №2

def format_string(string, length):
    if len(string) >= length:
        return string
    else:
        return ' ' * ((length - len(string)) // 2) + string

# №3


def factorial(n):
    if n < 2:
        return 1
    else:
        return n * factorial(n - 1)


def number_of_groups(n, k):
    return factorial(n) // (factorial(n - k) * factorial(k))
