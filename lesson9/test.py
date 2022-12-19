from pathlib import Path

p = Path('C:/Users/pc/Desktop/заняття/hw_kirill/lesson9')
print(p.parent)
print(p.name)
print(p.suffix)
print(p.exists())
print(p.is_dir())
print(p.is_file())

for i in p.iterdir():
    print(i.name)


# Режими відкриття
# 'r' -> відкриття на прочитання
# 'w' -> відкриття на запис, все, що є в файлі удаляється, якшо файла немає, створюється новий
# 'x' -> відкриття на запис, якшо файла немає, інакше буде помилка
# 'a' -> відкриття на дозапис, інформація потрапить у кінець
# 'b' -> відкриття в бінарному форматі(10110100011010010110100101100101010)
# 't' -> відкриття в текстовому режимі
# '+' -> відкриття на прочитання і на запис

# запис у файл
file = open('test1.txt', 'w')
count_symbols = file.write('hello!')
print(count_symbols)
file.close()

# читання і запис
file = open('test.txt', 'w+')
file.write('hello!')
file.seek(0)

first_three_symbols = file.read(5)
print(first_three_symbols)
file.close()

# читання і запис
file = open('test.txt', 'w', encoding='utf-8')
file.write('hello!htrsydtjdhgfdgzfhghdgscdvbfgnhjmmgfdsafgfjhjgfdsa\nfghjgfdsafghjgfdsafghjgfdsadfghjkhgfdsadfghjkhgfdsa')
file.close()

file = open('test.txt', 'r')
all_file = file.read()
print(all_file)
file.close()

file = open('test.txt', 'w', encoding='utf-8')
file.write('Hello world!\n')
file.write('Hello Ukraine!\n')
file.writelines(['Hi Sasha!\n', 'Hi Dima!\n', 'Hi Kirill\n'])
file.close()

file = open('test.txt', 'r', encoding='utf-8')
result = file.readlines()
print(result)
file.close()
