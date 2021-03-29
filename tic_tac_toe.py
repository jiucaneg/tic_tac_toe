# Крестики нолики моя первая игра на python

# Сделаем игровое поле по словарю
# в каких клавишах будет расположение (например: вверху слева, посередине справа и т. д.)
# и изночально его значения будут пустым пространством, а затем после каждого хода
# мы изменим значение в соответствии с выбором игрока

theBoard = {'7': ' ', '8': ' ', '9': ' ',
            '4': ' ', '5': ' ', '6': ' ',
            '1': ' ', '2': ' ', '3': ' '}

board_keys = []

for key in theBoard:
    board_keys.append(key)

# Создаем функцию выводящую на экран наше поле для игры в крестики нолики


def printBoard(board):
    print(board['7'] + '|' + board['8'] + '|' + board['9'])
    print('-+-+-')
    print(board['4'] + '|' + board['5'] + '|' + board['6'])
    print('-+-+-')
    print(board['1'] + '|' + board['2'] + '|' + board['3'])


# Создаем основную функцию для игры
def game():
    player = 'X'
    count = 0

    for i in range(10):
        printBoard(theBoard)
        print("Игрок," + player + ".Введите номер клетки!!!")

        move = input()

        if not move.isdigit():
            print("Введите целое число от 1 до 9")
            continue
        elif theBoard[move] == ' ':
            theBoard[move] = player
            count += 1
        else:
            print("Эта клетка уже занята.\nВведите номер другой клетки!!")
            continue

        # Теперь мы будем проверять, выиграл ли игрок X или O, для каждого хода после 5 ходов.
        if count >= 5:
            if theBoard['7'] == theBoard['8'] == theBoard['9'] != ' ':  # по верхней горизонтальной линии
                printBoard(theBoard)
                print("\nКонец игры.\n")
                print(" **** " + player + " выйграл. ****")
                break
            elif theBoard['4'] == theBoard['5'] == theBoard['6'] != ' ':  # по центральной горизонтальной линии
                printBoard(theBoard)
                print("\nКонец игры.\n")
                print(" **** " + player + " выйграл. ****")
                break
            elif theBoard['1'] == theBoard['2'] == theBoard['3'] != ' ':  # по нижней горизонтальной линии
                printBoard(theBoard)
                print("\nКонец игры.\n")
                print(" **** " + player + " выйграл. ****")
                break
            elif theBoard['1'] == theBoard['4'] == theBoard['7'] != ' ':  # по левой вертикальной линии
                printBoard(theBoard)
                print("\nКонец игры.\n")
                print(" **** " + player + " выйграл. ****")
                break
            elif theBoard['2'] == theBoard['5'] == theBoard['8'] != ' ':  # по центральной вертикальной линии
                printBoard(theBoard)
                print("\nКонец игры.\n")
                print(" **** " + player + " выйграл. ****")
                break
            elif theBoard['3'] == theBoard['6'] == theBoard['9'] != ' ':  # по правой вертикальной линии
                printBoard(theBoard)
                print("\nКонец игры.\n")
                print(" **** " + player + " выйграл. ****")
                break
            elif theBoard['7'] == theBoard['5'] == theBoard['3'] != ' ':  # по первой диагонали
                printBoard(theBoard)
                print("\nКонец игры.\n")
                print(" **** " + player + " выйграл. ****")
                break
            elif theBoard['1'] == theBoard['5'] == theBoard['9'] != ' ':  # по второй диагонали
                printBoard(theBoard)
                print("\nКонец игры.\n")
                print(" **** " + player + " выйграл. ****")
                break

                # Если ни X, ни O не выиграют, а доска заполнена, мы объявляем результат как «ничья»..
        if count == 9:
            print("\nКонец игры.\n")
            print("Ничья!!!")

        # Меняем игрока после каждого хода.
        if player == 'X':
            player = 'O'
        else:
            player = 'X'

            # Перезапуск игры
    restart = input("Хотите начать заново? Если да введите '1'.")
    if restart == "1":
        for key in board_keys:
            theBoard[key] = " "

        game()


if __name__ == "__main__":
    print('''Приветствую вас в игре "Крестики Нолики".
Нам дано поле из девяти клеток!!! Каждая клетка поля соответсвует циферному значению
keypad на клавиатуре. В игре учавствуют 2 игрока "X" и "0". По очереди они ставят 
в свободную клетку 'X' и '0' соответственно. Выигрывает игрок у которого первым получится 
занять три клетки подряд в одну линию (по горизонтали или вертикали, или диагонали).''')
    print('7' + '|' + '8' + '|' + '9')
    print('-+-+-')
    print('4' + '|' + '5' + '|' + '6')
    print('-+-+-')
    print('1' + '|' + '2' + '|' + '3')
    print("="*50)
    start = input("Хотите начать игру? Если да введите '1'.")
    if start == "1":
        for key in board_keys:
            theBoard[key] = " "

        game()