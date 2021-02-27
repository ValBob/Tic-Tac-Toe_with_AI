# write your code here

class WrongMoveError(BaseException):
    pass


class CellOccupiedError(WrongMoveError):
    pass


class NotNumberError(WrongMoveError):
    pass


class WrongCoordinatesError(WrongMoveError):
    pass


def print_table(table):
    print('-' * 9)
    for row in table:
        print('|', end=' ')
        for col in row:
            if col == '_':
                col = ' '
            print(col, end=' ')
        print('|')
    print('-' * 9)


def make_move(table):
    while True:
        coords = input('Enter the coordinates: ').split()
        row = coords[0]
        col = coords[1] if len(coords) == 2 else ""
        try:
            if bool((set(row) | set(col)) - set('0123456789')):  # check if row and col consist anything but digits
                raise NotNumberError
            elif not all((1 <= int(row) <= 3, 1 <= int(col) <= 3)):
                raise WrongCoordinatesError
            elif table[int(row) - 1][int(col) - 1] != '_':
                raise CellOccupiedError
        except NotNumberError:
            print('You should enter numbers!')
        except WrongCoordinatesError:
            print('Coordinates should be from 1 to 3!')
        except CellOccupiedError:
            print('This cell is occupied! Choose another one!')
        else:
            next_mark = 'X'
            if sum(row.count('X') for row in table) > sum(row.count('O') for row in table):
                next_mark = 'O'
            row, col = int(row) - 1, int(col) - 1
            table[row][col] = next_mark
            print_table(table)
            return table, row, col


def move_result(table, row, col):
    last_mark = table[row][col]
    win = False
    while True:
        for cell in range(3):
            if table[row][cell] != last_mark:
                break
            else:
                continue
        else:
            win = True
        if win:
            break
        for cell in range(3):
            if table[cell][col] != last_mark:
                break
            else:
                continue
        else:
            win = True
        if win:
            break
        if row == col:
            for cell in range(3):
                if table[cell][cell] != last_mark:
                    break
                else:
                    continue
            else:
                win = True
                print('\\ wins')
        if row + col == 2:
            for cell in range(3):
                if table[2 - cell][cell] != last_mark:
                    break
                else:
                    continue
            else:
                win = True
        break
    if win:
        print(f'{last_mark} wins')
    else:
        if sum(row.count('X') for row in table) + sum(row.count('O') for row in table) == 9:
            print('Draw')
        else:
            print('Game not finished')


initial = input('Enter the cells: ')
char_generator = (char for char in initial)
start_table = [[next(char_generator) for j in range(3)] for i in range(3)]

print_table(start_table)

current_table, row_, col_ = make_move(start_table)

move_result(current_table, row_, col_)
