def print_grid_3x3():
    print('-' * 9)
    print(f'| {cell[0]} {cell[1]} {cell[2]} |\n'
          f'| {cell[3]} {cell[4]} {cell[5]} |\n'
          f'| {cell[6]} {cell[7]} {cell[8]} |')
    print('-' * 9)


cell = [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']

coordinates = [13, 23, 33,
               12, 22, 32,
               11, 21, 31]

print_grid_3x3()

player_turn = 'O'
while ' ' in cell:
    coordinate = input('Enter the coordinate: > ').split()

    if ''.join(coordinate).isdigit() is False:
        print('You should enter numbers!')

    elif int(''.join(coordinate)) not in coordinates:
        print('coordinate should be from 1 to 3!')

    elif cell[coordinates.index(int(''.join(coordinate)))] != ' ':
        print('This cell is occupied! Choose another one!')

    elif 'O' in player_turn:
        cell[coordinates.index(int(''.join(coordinate)))] = 'X'
        player_turn = 'X'
        print_grid_3x3()

    elif 'X' in player_turn:
        cell[coordinates.index(int(''.join(coordinate)))] = 'O'
        player_turn = 'O'
        print_grid_3x3()

    wins = [cell[:3], cell[3:6], cell[6:9],
            cell[::3], cell[1::3], cell[2::3],
            cell[::4], cell[2:7:2]]

    if ['X', 'X', 'X'] in wins:
        print_grid_3x3()
        print('X wins')
        break

    elif ['O', 'O', 'O'] in wins:
        print_grid_3x3()
        print('O wins')
        break

else:
    print_grid_3x3()
    print('Draw')
