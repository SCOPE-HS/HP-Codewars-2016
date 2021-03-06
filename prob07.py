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

lines = mass_input(lines=int(input()))
for line in lines:
    words = line.split()
    common = ''
    for char in words[0]:
        for word in words[1:]:
            if char in word:
                common += char
                word = ''.join([x for x in word].pop(word.find(char)))
    p