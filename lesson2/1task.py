# Пользователь вводит число от 0 до 100. Подсчитайте, используя цикл while, сумму всех чисел от первого до введенного
# числа включительно в num.
# Результат поместить в переменную sum.
# Тесты будут:
# Помещать тестовые значения для переменной num: 20, 10, 5, 100
# И ожидать суммы в переменной sum: 210, 55, 15, 5050
num = int(input("Enter the integer (0 to 100): "))
sum = 0
# 5 -> 1+2+3+4+5
while num:  # while True  num = 0 -> False
    sum = sum + num
    num = num - 1

print(sum)
