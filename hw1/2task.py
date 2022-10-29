# Визначити парність/непарність числа яке приходить з консолі, перевірити чи більше чи менше за нуль,
# а також обробити помилку ValueError
num = 0
try:
    num = int(input('Input number: '))
except ValueError:
    print('Incorrect data! Try number')

if num > 0:
    if num % 2:
        result = "Positive odd number"
    else:
        result = "Positive even number"
elif num < 0:
    result = "Negative number"
else:
    result = "It is zero"

print(result)

