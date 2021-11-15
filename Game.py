import os
import Settings
import Map

Game_map = [i for i in Map.Game_map_str]


while True:
    Game_map[Settings.Player_pos] = "0"
    print(''.join(str(e) for e in Game_map))#Выводим карту и игрока на экран
    Com = input("Действие:")#Получаем дейсвие
    os.system('cls' if os.name == 'nt' else 'clear')#Очищаем консоль
    Game_map[Settings.Player_pos] = "."

    if Com == Settings.Move_key_forward:#шаг в перёд
        Settings.Last_player_pos = Settings.Player_pos
        Settings.Player_pos -= Settings.Line_length

    if Com == Settings.Move_key_back:#Шаг назад
        Settings.Last_player_pos = Settings.Player_pos
        Settings.Player_pos += Settings.Line_length

    if Com == Settings.Move_key_right:#Шаг в право
        Settings.Last_player_pos = Settings.Player_pos
        Settings.Player_pos += Settings.Length_step

    if Com == Settings.Move_key_left:#Шаг в лево
        Settings.Last_player_pos = Settings.Player_pos
        Settings.Player_pos -= Settings.Length_step

        
    if Game_map[Settings.Player_pos] == "#":#Обработка столкновений с стеной
        Settings.Player_pos = Settings.Last_player_pos
        continue


    if Com == Settings.ESC_key:#Завершение игры
        break




