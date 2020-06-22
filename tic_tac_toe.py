

grid = {
    0: [' ', ' ', ' '],
    1: [' ', ' ', ' '],
    2: [' ', ' ', ' '],
}


def change_grid(x: int, y: int, new: str):
    """Change value of grid[y][x] to new.

    Use this function to put 'X' or 'O' on the board.

    Args:
        x (int): X position on the board
        y (int): Y position on the board
        new (str): New value at position (x, y)

    Returns:
        None

    """
    grid[y][x] = new


def check_win(grid: dict):
    """Check for win and draw.

    Args:
        grid (dict): The dict for the board

    Returns:
        str: ``X`` or ``Y`` if not draw.
            Return ``draw`` if there is no whitespaces in lists of `grid`.

    """
    if (grid[0][0] == grid[0][1] == grid[0][2] or
            grid[0][0] == grid[1][0] == grid[2][0]):
        if grid[0][0] != ' ':
            return grid[0][0]

    if (grid[2][2] == grid[2][1] == grid[2][0] or
            grid[2][2] == grid[1][2] == grid[0][2]):
        if grid[2][2] != ' ':
            return grid[2][2]

    if (grid[0][1] == grid[1][1] == grid[2][1] or
            grid[1][0] == grid[1][1] == grid[1][2] or
            grid[0][0] == grid[1][1] == grid[2][2] or
            grid[0][2] == grid[1][1] == grid[2][0]):
        if grid[1][1] != ' ':
            return grid[1][1]

    elif ' ' not in grid[0] and ' ' not in grid[1] and ' ' not in grid[2]:
        return 'draw'


def formatted(grid: dict):
    """function for making a board with the values in `grid`

    Args:
        grid (dict): The dict for the board

    Returns:
        str: The formatted string based on the values in `grid`

    """
    res = '  +-----------+\n'
    res += f'3 | {grid[2][0]} | {grid[2][1]} | {grid[2][2]} |\n'
    res += '  +-----------+\n'
    res += f'2 | {grid[1][0]} | {grid[1][1]} | {grid[1][2]} |\n'
    res += '  +-----------+\n'
    res += f'1 | {grid[0][0]} | {grid[0][1]} | {grid[0][2]} |\n'
    res += 'y +-----------+\n'
    res += '  x 1   2   3  '

    return res


def main():
    x_turn = True

    while True:
        print(formatted(grid))
        print()

        if check_win(grid) in ('X', 'Y'):
            print(f'The winner is: {check_win(grid)}!')
            break
        elif check_win(grid) == 'draw':
            print('It\'s a draw!')
            break

        try:
            pos = input(f'{"X" if x_turn else "O"} > ').split(' ')
            x = int(pos[0])
            y = int(pos[1])

            if grid[y-1][x-1] == ' ':
                change_grid(x-1, y-1, "X" if x_turn else "O")
                x_turn = not x_turn
            else:
                print(f'There is already an {grid[y-1][x-1]} at ({x}, {y})!')

        except KeyboardInterrupt:
            quit()
        except Exception:
            print('Invalid position! Expected format: ', end='')
            print('(x y) without parentheses and x <= 3, y <= 3.')

        print()


if __name__ == '__main__':
    main()
