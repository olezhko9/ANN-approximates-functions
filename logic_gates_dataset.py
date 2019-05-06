logic_dataset = [
    # AND
    [[1, 0, 0], [0]],
    [[1, 0, 1], [0]],
    [[1, 1, 0], [0]],
    [[1, 1, 1], [1]],
    # OR
    [[2, 0, 0], [0]],
    [[2, 0, 1], [1]],
    [[2, 1, 0], [1]],
    [[2, 1, 1], [1]],
    # XOR
    [[3, 0, 0], [0]],
    [[3, 0, 1], [1]],
    [[3, 1, 0], [1]],
    [[3, 1, 1], [0]],
    # X -> Y
    [[4, 0, 0], [1]],
    [[4, 0, 1], [1]],
    [[4, 1, 0], [0]],
    [[4, 1, 1], [1]],
    # NOT
    [[-1, 0, 0], [1]],
    [[-1, 1, 1], [0]],
    # X | Y similar to NAND
    [[-2, 0, 0], [1]],
    [[-2, 0, 1], [1]],
    [[-2, 1, 0], [1]],
    [[-2, 1, 1], [0]],
    # X ↓ Y similar to NOR
    [[-3, 0, 0], [1]],
    [[-3, 0, 1], [0]],
    [[-3, 1, 0], [0]],
    [[-3, 1, 1], [0]],
    # X = Y similar to NXOR
    [[-4, 0, 0], [1]],
    [[-4, 0, 1], [0]],
    [[-4, 1, 0], [0]],
    [[-4, 1, 1], [1]],
]