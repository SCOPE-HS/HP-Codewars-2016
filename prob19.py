TREE = {}

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

def children(item, n, raw):
    lofchildren = [x for x in TREE[item]]
    for child in lofchildren:
        if child[1] not in tree:
            raw.append((child[0] * n, child[1]))
        else:
            children(child[1], child[0] * n, raw)


inputs = mass_input(lines=int(input()))

for line in inputs:
    args = line.split()
    name, num_ingredients = args[0], args[1]
    ingredients = []
    for i in range(2, len(args), 2):
        ingredients.append((args[i], args[i+1]))
    print(name, num_ingredients, ingredients)
    TREE[name] = ingredients

recipes_needed = mass_input(end='GO')
for item in recipes_needed:
    print(TREE)
