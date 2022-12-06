from lesson7.task1 import sanitize_phone_number
# Japan	JP	+81
# Singapore	SG	+65
# Taiwan	TW	+886
# Ukraine	UA	+380
# Напишите функцию get_phone_numbers_for_countries, которая будет:
#
# Принимать список телефонных номеров.
# Нормализовать полученный список телефонов клиентов с помощью нашей функции sanitize_phone_number.
# Сортировать телефонные номера по указанным в таблице странам.
# Возвращать словарь со списками телефонных номеров для каждой страны в следующем виде:
# {
#     "UA": [<здесь список телефонов>],
#     "JP": [<здесь список телефонов>],
#     "TW": [<здесь список телефонов>],
#     "SG": [<здесь список телефонов>],
# }
# Если не удалось сопоставить код телефона с известными, этот телефон должен быть добавлен в
# список словаря с ключом "UA".


def get_phone_numbers_for_countries(list_phones: list) -> dict:
    list1 = []
    list2 = []
    list3 = []
    list4 = []
    codes = ['JP', 'SG', 'TW', 'UA']
    for phone in list_phones:
        new_phone = sanitize_phone_number(phone)
        if new_phone.startswith('81'):
            list1.append(new_phone)
            continue
        if new_phone.startswith('65'):
            list2.append(new_phone)
            continue
        if new_phone.startswith('886'):
            list3.append(new_phone)
            continue
        else:
            list4.append(new_phone)
    return {codes[0]: list1, codes[1]: list2, codes[2]: list3, codes[3]: list4}


print(get_phone_numbers_for_countries(['  +81(423)', '  +65(4324432)-(432)  ', ' +886(10)-(432)', ' +38093731(6048)  ']))

