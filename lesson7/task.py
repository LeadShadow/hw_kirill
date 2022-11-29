first_string = 'Hello'
second_string = 'Hello'
print(id(first_string) == id(second_string))
print(id(first_string))
print(id(second_string))

one_line_text = 'ajwdkahwdajwdkhawkdhawdkawhdkahwdakhwdahdawdhawkdawdawdawdawdawdawdawdawd.\n' \
                'dawdawdawdawdawdawdawdawdawdawdawdawdawdawdawdawdawdadwwadwadawdawdawdawdawd'

print(one_line_text)

print("spam " "eggs" == "spam eggs")


print('dawdawdawdaw\nfejnjfesjonefsjefs')


s = 'Hi there!'
start = 0
end = 7

print(s.find('er'))
s1 = 'Some words'
print(s.rfind('o', 0, 10))

s2 = 'I am learning Python. I have got some skills.'
sentences = s2.split('. ')  # str -> list

print(sentences)

text = '. '.join(sentences)  # list -> str
print(text)
user_input = input('Input string: ')

if user_input.strip() == 'hello':
    print('hello')

clean_string = user_input.strip()
print(clean_string)

print(clean_string + 'dwadaw')

number = '+38093(731)(6048)'
clean_number = number.replace('+', '')
clean_number = clean_number.replace('(', '')
print(clean_number)  # -> 38093731)6048)
clean_number = clean_number.replace(')', '')
print(clean_number)
print(number[1:])


string_hook = 'TestHook'
prefix_hook = string_hook.removeprefix('Test')
print(prefix_hook)

string_hook1 = 'TestHook'
suffix_hook = string_hook1.removesuffix('Hook')
print(suffix_hook)


string_1 = 'oleksandr'

print(string_1.capitalize())

