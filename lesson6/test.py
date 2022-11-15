set_1 = {1, 2, 3}


set_1.add(4)
print(set_1)
set_1.discard(5)
print(set_1)


set_2 = {1, 2, 10, 12, 15}
list_1 = list('hello')
print(list_1)
print(set_2)

print(set_1 & set_2)  # end
print(set_1 ^ set_2)  # xor
print(set_1 | set_2)  # or


points = {
    (0, 0): 'O',
    (1, 1): 'A',
    (2, 2): 'B'
}

tuple_1 = (4,)


s = 'HELLO WORLD'
print(s[0])
print(s[-1])
print(s + '!')


print(s.lower())
print(s.startswith('HE'))
s1 = 'hello.png'
print(s1.endswith('png'))


password = 'qwerty123'
if 'qwerty' in password and '123' in password:
    print('This password is to weak!')


user = {
    'name': 'Bill',
    'surname': 'Samus',
    'age': 20
}

if 'age' in user:
    print(f"User is {user['age']} years old.")

password = input('Password: ')
if len(password) < 8:
    print('Your password is too short')
