# Розробити банкового помічника, який буде допомагати обраховувати гривні в долари і навпаки
# в залежності від вибору(умову if data == <вибір>) і в залежності від вибору обрахувати і обробити
# помилку ValueError якщо з консолі вводять в змінну sum не число

dollar_rate = 40.5
print('Input 1 if you want transit hryvnias to dollars')
print('Input 2 if you want transit dollars to hryvnias')
data = input('Choose number: ')
sum = 1

if data == '1':
    try:
        sum = int(input('Enter the quantity: '))
    except ValueError:
        print('Inccorect data')
    result = sum / dollar_rate
    print(result)
elif data == '2':
    try:
        sum = int(input('Enter the quantity: '))
    except ValueError:
        print('Inccorect data')
    result = sum * dollar_rate
    print(result)
