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
    common = ''
    words = line.split()
    for word in range(len(words)):
        words[i] = list(word)
    print(words)
    for char in words[0]:
        if all(char in word for word in words):
            common += char
            for word in words:
                word.pop(word.find(char))