my_tuple1 = (1, 2, 3)
my_tuple2 = (1, 2, 3, 4)

sum = 0
for i in my_tuple1:
    sum += i
    print(sum)
print(sum)

dict1 = {}
dict2 = dict()
print(type(dict1))
print(type(dict2))

some_dict = {
    'key': 'value',
    1: 'one'
}


dict3 = {'key': 'value'}
dict3['new_key'] = 'new_value'
print(dict3)
print(dict3['key'])


dict_for_kirill = {
    'name': 'Kirill',
    'age': 14,
    'experience_in_pr': '4 month'
}

for k, v in dict_for_kirill.items():
    print(f'{k}: {v}')


# рекурсія
# 3! -> 3 * 2! -> 3 * 2 * 1
# 4! -> 4 * 3! -> 4 * 3 * 2! -> 4 * 3 * 2 * 1
# 5!

def factorial(n):
    if n <= 1:
        return 1
    else:
        return n * factorial(n - 1) #  -> 5 * 4! -> 4 * 3! -> 3 * 2! -> 2 * 1


print(factorial(5))  # -> 5 * 4 * 3 * 2 * 1

print('hello ' + 'world')
