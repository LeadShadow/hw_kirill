# Виконайте завдання, щоб визначити парне чи ні, за допомогою тернарного оператора.

# Програма встановлює значення змінної is_even у True або False, залежно від того,
# чи є число змінної num парним або непарним.

# Підказка: перевірка на парність виконується порівнянням залишку від розподілу на 2 з 0 або 1.
# Нагадаємо, залишок від розподілу можна отримати після операції %


# тернарний оператор -> скорочений варіант if else
num = int(input("Enter an integer number: "))

is_even = True if num % 2 else False

if num % 2:
    is_even = True
else:
    is_even = False
# результат іф - if - умова - else - результат елсе
