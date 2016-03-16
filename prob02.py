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

rates =[int(i) for i in mass_input(end='0')]

for rate in rates:
    weeks = 10000 / rate
    rweeks = str(weeks).split('.')[0]
    print('{} gallons per week will last {} weeks'.format(rate, rweeks))