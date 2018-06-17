def get_quadrant_number(x, y):
    if x == 0 or y == 0:
        raise ValueError()

    tup = {
        (1, 1): 1,
        (-1, 1): 2,
        (-1, -1): 3,
        (1, -1): 4
    }

    return tup.get((x, y))