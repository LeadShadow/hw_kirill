my_list = list()
list1 = []
print(my_list)
not_empty = [1, 2, 'string']
print(not_empty[2])

for i in not_empty:
    print(i)

some_str = 'This is awesome string.'
print(len(some_str))
print(some_str[:22])
numbers_ = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
odd_numbers = numbers_[0:10:2]
even_numbers = numbers_[1:10:2]
three_numbers = numbers_[2:10:3]
print(odd_numbers)
print(even_numbers)
print(three_numbers)
numbers_copy = numbers_[:]
print(numbers_copy)

numbers2 = ['a', 'b']
numbers2.append('c')
print(numbers2)

list3 = [1, 2, 3]
list3.clear()
print(list3)

chars = ['a', 'b']
print(chars)
chars.insert(0, 'c')
print(chars)

print(chars.index('a'))
chars.append('a')
chars.append('a')
print(chars.count('a'))
chars.append('k')
chars.append('d')
print(sorted(chars))
print(chars)
print(chars[::-1])
chars.reverse()
print(chars)
chars_copy = chars.copy()
print(chars == chars_copy)

dict_chars = {'a': 1, 'b': 2}
b_num = dict_chars.pop('b')
print(dict_chars)

dict_chars.update({'c': 3})
print(dict_chars)

c_idx = dict_chars.get('c', 1)
print(c_idx)
