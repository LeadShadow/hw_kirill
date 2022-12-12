'''
Задача: Поиск email
- алфавит, используемый для названия email, — английский

- префикс (все, что находится до символа @) начинается с латинской буквы и может содержать любое число или букву, включая нижнее подчеркивание и символ точки, состоит минимум из двух символов

- суффикс письма (все, что находится после символа @) состоит только из букв английского алфавита, состоит из двух частей, разделенных точкой, и доменное имя верхнего уровня не может быть меньше двух символов (все, что после точки)
'''

import re
# olexandr.samus.2004@gmail.com
text = "Ima.Fool@iana.org Ima.Fool@iana.o Fool1@iana.org first_last@iana.org first.middle.last@iana.or a@test.com " \
       "abc111@test.com.net 12Fool1@iana.org, olexandr.samus.2004@gmail.com"

# Найти email
result = re.findall(r'\b[a-zA-Z]{2}[\w\.]+@[a-zA-Z]+\.[a-zA-Z]{2,}', text)
print(result)