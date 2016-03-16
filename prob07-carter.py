import string

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


def next_dash(string, position=0):
    """Returns the index of the next "-" in the string."""
    while string[position] != '-':
        position = (position + 1) % len(string)
    return position


alphabet = string.ascii_uppercase
skips = {char: (i % 5) + 1 for i, char in enumerate(alphabet)}
skips[' '] = 6

lines = mass_input(lines=1)

for l in lines:
    output = l[0] + ('-' * (len(l) - 1))
    i = 0
    current = l[0]
    while '-' in l:
        for __ in range(skips[l[i]]):
            i = next_dash(l, i)
