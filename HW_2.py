# 2- Создайте программу для игры с конфетами человек против человека.

# Условие задачи: На столе лежит 2021 конфета. Играют два игрока делая ход друг после друга. 

# Первый ход определяется жеребьёвкой. За один ход можно забрать не более чем 28 конфет. 

# Тот, кто берет последнюю конфету - проиграл.

# a) Добавьте игру против бота

# b) Подумайте как наделить бота ""интеллектом""

from random import randint

def privet ():
    Player_1 = input ("Введите имя первого игорока: ")
    Variant_Game = check_option_game()
    if Variant_Game == 1:
        Player_2 = input ("Введите имя второго игорока: ")
    elif Variant_Game == 2:
        Player_2 = "Компьютер"
    else:
        Player_2 = "Суперкомпьютер"
    Bank = check_numbers("Введите количество конфет всего: ", "Некорректный ввод, попробуйте еще раз")
    Number = check_numbers("Введите количество конфет, которое можно взять игроку за один ход: ", "Некорректный ввод, попробуйте еще раз")
    return [Player_1, Player_2, Bank, Number, Variant_Game]

def whose_first_move(player_1, player_2):
    random_move = randint(0,1)
    if random_move == 0:
        print(f"Первый ход делает: {player_1}")
        return 0
    else:
        print(f"Первый ход делает: {player_2}")
        return 1

def Game(player_1, player_2, bank, max_move):
    number_move = whose_first_move(player_1, player_2)
    Number_of_each_player = check_Number_of_each_player("Ваш ход: ", max_move)
    bank -= Number_of_each_player
    while bank > 0:
        Number_of_each_player = check_Number_of_each_player("Ход следующиего игрока: ",max_move)
        number_move += 1
        bank -= Number_of_each_player
    if number_move%2 == 0:
        print(f"Выиграл(а): {player_1}")
    else:
        print(f"Выиграл(а): {player_2}")

def Game_with_computer(player_1, player_2, bank, max_move): # включает варианты игры с ботом и умным ботом в зависимости от имени функции Privet
    number_move = whose_first_move(player_1, player_2)
    move_order = number_move    
    while bank > 0:
        if move_order == 0:
            Number_of_each_player = check_Number_of_each_player(f"Ход {player_1}: ",max_move)
            number_move += 1
            bank -= Number_of_each_player
            move_order = 1
        else:
            if player_2 == "Компьютер":
                Number_of_each_player = randint(1,max_move)
                print(f"Ход {player_2}: {Number_of_each_player}")
            else:
                if bank/max_move > 1:
                    Number_of_each_player = max_move
                    print(f"Ход {player_2}: {Number_of_each_player}")
                elif bank//max_move == 0 and bank-1 != 0:
                    Number_of_each_player = bank - 1
                    print(f"Ход {player_2}: {Number_of_each_player}")
                elif bank//max_move == 1:
                    Number_of_each_player = max_move - 1 
                    print(f"Ход {player_2}: {Number_of_each_player}")
                else:
                    Number_of_each_player = 1
                    print(f"Ход {player_2}: {Number_of_each_player}")
            number_move += 1
            bank -= Number_of_each_player
            move_order = 0
    if number_move%2 == 0:
        print(f"Выиграл(а): {player_1}")
    else:
        print(f"Выиграл(а): {player_2}")

def check_numbers(str1, str2):
    result = input(f"{str1}")
    while 1:
        if not result.isdigit():
            result = input(f"{str2}")
            continue
        else: 0
        break
    return int(result)

def check_Number_of_each_player(str, number_of_move):
    result = input(f"{str}")
    while 1:
        if not result.isdigit():
            result = input("Попробуйте еще раз: ")
            continue
        elif int(result) < 1 or int(result) > number_of_move:
            result = input("Вы вводите другое количество конфет, чем положено. Попробуйте еще раз: ")
        else: 0
        break
    return int(result)

def check_option_game():
    result = input("Введите вариант игры: 1 - другой игрок, 2 - компьютер, 3 - суперкомпьютер: ")
    while 1:
        if not result.isdigit():
            result = input("Попробуйте еще раз: ")
            continue
        elif not int(result) in [1,2,3]:
            result = input("Попробуйте еще раз: ")
        else: 0
        break
    return int(result)

def Options(Player_1, Player_2, Bank, Number, Variant_Game):
    if Variant_Game == 1:
        return Game(Player_1, Player_2, Bank, Number)
    else:
        return Game_with_computer(Player_1, Player_2, Bank, Number)

def Game_main():
    data = privet() # Возвращает лист [Имя игрока 1, Имя игрока 2, банк из конфет, маскимальное количество конфет за ход]
    Options(data[0], data[1], data[2], data[3], data[4]) # Включает различные алгоритмы игры и возвращает имя победителя

Game_main()

        
        
           


