import random


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


def human_input(table):
    while True:
        coordinates = input('Enter the coordinates: ').split()
        row = coordinates[0]
        col = coordinates[1] if len(coordinates) == 2 else ""
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
            row, col = int(row) - 1, int(col) - 1
            return row, col


def make_move(table, row, col):
    while True:
        next_mark = 'X'
        if sum(row.count('X') for row in table) > sum(row.count('O') for row in table):
            next_mark = 'O'
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
        return True
    else:
        if sum(row.count('X') for row in table) + sum(row.count('O') for row in table) == 9:
            print('Draw')
            return True
        else:
            return False


def easy_level(table):
    print('Making move level "easy"')
    empty_cells = [(i, j) for i in range(3) for j in range(3) if table[i][j] == '_']
    random.seed()
    row, col = empty_cells[random.randint(0, len(empty_cells) - 1)]
    return row, col


start_table = [['_' for j in range(3)] for i in range(3)]

print_table(start_table)

cur_table = start_table
cnt = 0
while True:
    if cnt % 2 == 0:
        row_, col_ = human_input(cur_table)
    else:

        row_, col_ = easy_level(cur_table)
    make_move(cur_table, row_, col_)
    cnt += 1
    if move_result(cur_table, row_, col_):
        break
