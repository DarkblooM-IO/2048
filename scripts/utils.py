def rotate90(l: list[list], size: int, repeat: int = 1) -> list[list]:
    for _ in range(repeat):
        for x in range(0, int(size / 2)):
            for y in range(x, size - x - 1):
                buffer = l[x][y]
                l[x][y] = l[y][size - 1 - x]
                l[y][size - 1 - x] = l[size - 1 - x][size - 1 - y]
                l[size - 1 - x][size - 1 - y] = l[size - 1 - y][x]
                l[size - 1 - y][x] = buffer
    return l

if __name__ == "__main__":
    l = [[i for i in range(4)] for ii in range(4)]
    print(l)
    print(rotate90(l, len(l)))
