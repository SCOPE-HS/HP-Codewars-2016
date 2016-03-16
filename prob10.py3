import re

xwins = [
'XXX......', '...XXX...', '......XXX',
'X..X..X..', '.X..X..X.', '..X..X..X',
'X...X...X', '..X.X.X..']
owins = [win.replace('X', 'O') for win in xwins]

def mass_input(prompt=None, lines=None, end=None):
    """Returns a list of lines of input."""

    assert lines is None or end is None  # Can't do both
    assert lines is not None or end is not None  # Can't have neither

    inputs = []

    if prompt is not None:
        print(prompt, end='')

    if lines is not None:
        assert type(lines) is int
        for __ in range(lines):
            inputs.append(input())

    elif end is not None:
        assert type(end) is str
        inputs.append(input())
        while inputs[-1] != end:
            inputs.append(input())
        assert inputs.pop(-1) == end

    return inputs

def printboard(board):
    """Prints a tic-tac-toe board."""
    assert len(board) == 9
    print(board[:3])
    print(board[3:6])
    print(board[6:])

games = mass_input(end='=========')

for game in games:
    winner = None
    for x in xwins:
        if re.match(x, game) is not None:
            win = x
            winner = 'X'
    for o in owins:
        if re.match(o, game) is not None:
            win = o
            winner = 'O'
    if winner is None:
        print('There was a tie.')
        printboard(game)
    else:
        print('Player {} won.'.format(winner))
        edited = ''
        for i, char in enumerate(win):
            if char == '.':
                edited += game[i]
            elif char in 'XO':
                edited += '$'
        printboard(edited)
    print()  # Blank line
