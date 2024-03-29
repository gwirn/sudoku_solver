def possible(y, x, n):
    global arr
    for i in range(0, 9):
        if arr[y][i] == n:
            return False
    for i in range(0, 9):
        if arr[i][x] == n:
            return False
    x0 = (x // 3) * 3
    y0 = (y // 3) * 3
    for i in range(0, 3):
        for j in range(0, 3):
            if arr[y0 + i][x0 + j] == n:
                return False
    return True


def solve():
    global arr
    for y in range(9):
        for x in range(9):
            if arr[y][x] == 0:
                for n in range(1, 10):
                    if possible(y, x, n):
                        arr[y][x] = n
                        solve()
                        arr[y][x] = 0
                return
    # print(np.matrix(arr))
    for i in arr:
        print(i)


"""
arr = [
    [5, 3, 0, 0, 7, 0, 0, 0, 0],
    [6, 0, 0, 1, 9, 5, 0, 0, 0],
    [0, 9, 8, 0, 0, 0, 0, 6, 0],
    [8, 0, 0, 0, 6, 0, 0, 0, 3],
    [4, 0, 0, 8, 0, 3, 0, 0, 1],
    [7, 0, 0, 0, 2, 0, 0, 0, 6],
    [0, 6, 0, 0, 0, 0, 2, 8, 0],
    [0, 0, 0, 4, 1, 9, 0, 0, 5],
    [0, 0, 0, 0, 8, 0, 0, 7, 9],
]
"""
arr = [
    [9, 0, 0, 0, 0, 0, 0, 0, 4],
    [0, 3, 0, 0, 7, 0, 6, 9, 0],
    [0, 0, 2, 8, 0, 0, 0, 0, 0],
    [0, 5, 0, 0, 0, 0, 0, 0, 1],
    [0, 0, 0, 0, 4, 0, 0, 0, 3],
    [8, 0, 0, 7, 0, 0, 4, 5, 0],
    [3, 0, 0, 0, 0, 9, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 1, 0],
    [0, 9, 0, 0, 6, 0, 5, 7, 0],
]
solve()
