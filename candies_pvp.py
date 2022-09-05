def correct_value(value, players, turn):
    result = input(f'{players[turn]}, твоя очередь брать конфеты: ')
    while not result.isdigit or not (29 > int(result) > 0) or int(result) > value:
        if value >= 28:
            result = input(f'{players[turn]}, можно вводить значения только от 1 до 28: ')
        else:
            result = input(f'{players[turn]}, можно вводить значения только от 1 до {value}: ')
    return int(result)


def player_init():
    player_1 = input('\nВведите имя первого игрока: ')
    player_2 = input('Введите имя второго игрока: ')
    return player_1, player_2


def players_draw(player_1, player_2):
    from random import randint as r
    draw = r(1, 2)
    if draw == 1:
        print(f'\nПо результатам жеребьевки первым ходит {player_1}!')
        return {1: player_1, 2: player_2}
    else:
        print(f'\nПо результатам жеребьевки первым ходит {player_2}!')
        return {1: player_2, 2: player_1}


def game_candies(value, players):
    turn = 1
    while value > 0:
        if turn == 1:
            move = correct_value(value, players, turn)
            value -= move
            if value == 0:
                print(f'\n{players[turn]} ПОБЕДИЛ!!!')
                break
            print(f'\nОсталось конфет: {value}\n')
            turn = 2
        if turn == 2:
            move = correct_value(value, players, turn)
            value -= move
            if value == 0:
                print(f'\n{players[turn]} ПОБЕДИЛ!!!')
                break
            print(f'\nОсталось конфет: {value}\n')
            turn = 1


count_candies = 100
print('___ИГРА В КОНФЕТЫ___')
print('Брать со стола можно от 1 до 28 конфет за раз')
print('Кто последний делает ход - тот победил!')
player_1, player_2 = player_init()
players = players_draw(player_1, player_2)
print(f'\nКолличество конфет на столе: {count_candies}\n')
game_candies(count_candies, players)