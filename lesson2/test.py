from time import sleep
# ітерація - повторення

# два види циклів for, while
# for <тимчасова змінна> in fruit
# fruit = 'apple'
#
# for i in fruit:
#     print(i)

# while

a = 0
while True:
    a = a + 1
    print(a)
    if a >= 20:
        break


while True:
    user_input = input('Input some text(exit that close program) ')
    print(user_input)
    if user_input == 'exit':
        break


a = 0
while a < 10:
    a = a + 1
    if not a % 2:  # a % 2 == 0
        continue
    print(a)
