import sys

place = [["-", "-", "-"],
        ["-", "-", "-"],
        ["-", "-", "-"]]

def verify(f, gamer):
    def verify_cell(b1, b2, b3, gamer):
        if b1 == gamer and b2 == gamer and b3 == gamer:
            return True
    for q in range(3):
        if verify_cell(f[q][0], f[q][1], f[q][2], gamer) or \
        verify_cell(f[0][q], f[1][q], f[2][q], gamer) or \
        verify_cell(f[0][0], f[1][1], f[2][2], gamer) or \
        verify_cell(f[2][2], f[1][1], f[0][2], gamer):
            return True
    return False

def draw_place(a):
    print("  0 1 2")
    for i in range(len(place)):
        print(str(i), *place[i])
    print("")

def gamer_type(a):
    while True:
        typing = input("Введите номер строки и номер столбца через пробел: ").split()
        print("")
        if len(typing) != 2:
            print("Введите две координаты через пробел.")
            print("")
            continue
        if not (typing[0].isdigit() and typing[1].isdigit()):
            print("Введите координаты цифрами (через пробел).")
            print("")
            continue
        x, y = map(int, typing)
        if not (x >=0 and x < 3 and y >= 0 and y < 3):
            print("Введите координаты в диапазоне от \"0\" до \"2\".")
            print("")
            continue
        if a[x][y] != "-":
            print("Эта ячейка занята. Введите координаты пустой ячейки.")
            print("")
            continue
        break
    return x,y

def game_all(place):
    counter = 0
    while True:
        if counter%2 == 0:
            gamer = "x"
        else:
            gamer = "o"
        draw_place(place)
        x,y = gamer_type(place)
        place[x][y] = gamer
        if counter == 9:
            print("Ничья.")
        if verify(place, gamer):
            print(f"Выиграл {gamer}")
            break
        counter += 1

print("")
print("*"*15)
print("Крестики-нолики.")
print("*"*15)
print("")
print("Первым ходит \"х\".")
print("")
print("Это - поле для игры:\n")
game_all(place)
while True:
    print("")
    keep_on = input("Продолжить игру? (английские \"y\" или \"n\"): ")
    if keep_on == "y":
        place = [["-", "-", "-"],
                ["-", "-", "-"],
                ["-", "-", "-"]]
        print("")
        game_all(place)
        continue
    elif keep_on == "n":
        print("")
        print("Игра закончена.")
        sys.exit()
        continue
    else:
        print("Введите только одно из двух: (английские) \"y\" или \"n\".")
        continue
    break

sys.exit()
