# В предыдущей задаче мы записали сотрудников в файл в следующем виде:

# Robert Stivenson, 28
# Alex Denver, 30
# Drake Mikelsson, 19
# Выполним теперь обратную задачу и создадим функцию read_employees_from_file(path),
# которая будет читать данные из файла и возвращать список сотрудников в виде:

# ['Robert Stivenson, 28', 'Alex Denver, 30', 'Drake Mikelsson, 19']
# Помните про присутствие символа конца строки \n при чтении данных из файла.
# Его необходимо убирать при добавлении прочитанной строки в список.

# Требования

# прочтите содержимое файла, используя режим "r".
# мы пока не используем менеджер контекста with
# верните из функции список сотрудников из файла
from pathlib import Path
p = Path('C:/Users/pc/Desktop/заняття/hw_kirill/lesson10/text.txt')


def read_employees_from_file(path: Path):
    file = open(path, 'r', encoding='utf-8')
    line = file.readlines()
    new_list = []
    for i in line:
        new_list.append(i.replace('\n', ''))
    file.close()
    return new_list


if __name__ == "__main__":
    print(read_employees_from_file(p))
