# 1- Напишите программу, удаляющую из текста все слова, содержащие ""абв"".
# 'абвгдейка - это передача' = >" - это передача"

def del_words(user_string: str, del_element: str):
    lst = user_string.split()
    new_lst = [x for x in lst if not del_element in x]
    result = " "
    return result.join(new_lst)

print(del_words('абвгдейка - это передача', 'абв'))