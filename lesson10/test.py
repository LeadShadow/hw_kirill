from task2 import total_salary, p
fh = open('text.txt', 'w+')
fh.close()
with open(p, 'r') as fh:
    print(total_salary(p))


# 1010101001001010
with open('data.bin', 'wb') as file:
    file.write(b'Hello world!')

