def weak_point(matrix):
    x = 0
    sumrow = -1
    for row in range(len(matrix)):
        sum = 0
        for column in range(len(matrix[0])):
            sum += matrix[row][column]
        if sumrow == -1:
            sumrow = sum
        elif sumrow > sum:
            x = row
    y = 0
    sumcolumn = -1
    for column in range(len(matrix[0])):
        sum = 0
        for row in range(len(matrix)):
            sum += matrix[row][column]
        if sumcolumn == -1:
            sumcolumn = sum
        elif sumcolumn > sum:
            y = column

    return x, y  # [0, 0]

print(list(weak_point([[7, 2, 4, 2, 8],
                            [2, 8, 1, 1, 7],
                            [3, 8, 6, 2, 4],
                            [2, 5, 2, 9, 1],
                            [6, 6, 5, 4, 5]])))

if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert isinstance(weak_point([[1]]), (list, tuple)), "The result should be a list or a tuple"
    assert list(weak_point([[7, 2, 7, 2, 8],
                            [2, 9, 4, 1, 7],
                            [3, 8, 6, 2, 4],
                            [2, 5, 2, 9, 1],
                            [6, 6, 5, 4, 5]])) == [3, 3], "Example"
    assert list(weak_point([[7, 2, 4, 2, 8],
                            [2, 8, 1, 1, 7],
                            [3, 8, 6, 2, 4],
                            [2, 5, 2, 9, 1],
                            [6, 6, 5, 4, 5]])) == [1, 2], "Two weak point"
    assert list(weak_point([[1, 1, 1],
                            [1, 1, 1],
                            [1, 1, 1]])) == [0, 0], "Top left"