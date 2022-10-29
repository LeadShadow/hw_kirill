# Строка — это итерируемый объект, а, значит, мы можем использовать ее в цикле for.
# Подсчитайте в заданной строке message количество вхождений символа из переменной search.
# Результат поместите в переменную result.
a = 123
message = f"Never argue with stupid people, {a} they will drag you down to their level and then beat you with experience."
search = "1"
result = 0
for i in message:
    if i == search:
        result += 1

print(result)



