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

words = mass_input(lines=int(input()))

for word in words:
    padding = ' ' * (len(word) - 1)
    padded = padding + word + padding
    for i in range((len(word) * 2) - 1):
        print(padded[i:i+len(word)])

    print()  # Blank line at end