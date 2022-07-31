# 4- Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных.
# Входные и выходные данные хранятся в отдельных текстовых файлах



def RLE_algorithm(text):
    result = ""
    i = 1
    count = 1
    while i < (len(text)):
        if str(text[i]) == str(text[i-1]):
            count +=1
            i +=1
        elif str(text[i]) != str(text[i-1]) and count > 1:
            result += f"{count}{text[i-1]}" 
            i +=1
            count = 1
        else:
            result += f"{count}{text[i-1]}"
            i+=1
    result += f"{count}{text[i-1]}"
    return result

def RLE_algoritm_negativ(text:str):
    result = ""
    for char in text:
        if char.isdigit():
            count = int(char)
        else:
            result+=char*int(count)
            count = 0 
    return result




with open("f1.txt", "r") as data:
    text_1 = data.read()

print(RLE_algorithm(text_1))

with open("f2.txt", "r") as data:
    text_2 = data.read()

print(RLE_algoritm_negativ(text_2))




