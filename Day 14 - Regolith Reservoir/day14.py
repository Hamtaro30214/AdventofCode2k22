def main(part2=False):
    with open('day14.txt') as f:
        data = f.read().split('\n')

    grid = set()
    for line in data:
        points = line.split(' -> ')
        prev = None
        for point in points:
            col, row = map(int, point.split(','))
            if prev:
                if col - prev[0]:
                    for i in range(min(col, prev[0]), max(col, prev[0]) + 1):
                        grid.add((i, row))
                else:
                    # update grid by row if col is empty
                    for i in range(min(row, prev[1]), max(row, prev[1]) + 1):
                        grid.add((col, i))
            prev = (col, row)

    # get number where is floor based on highest row from grid
    ground = max(i[1] for i in grid)
    dropped_sand = 0

    while True:
        sand = (500, 0)  # drop point of sand
        while True:
            if (sand[0], sand[1] + 1) not in grid:
                sand = (sand[0], sand[1] + 1)
            elif (sand[0] - 1, sand[1] + 1) not in grid:
                sand = (sand[0] - 1, sand[1] + 1)
            elif (sand[0] + 1, sand[1] + 1) not in grid:
                sand = (sand[0] + 1, sand[1] + 1)
            else:
                grid.add(sand)
                break

            # check if ground is full
            if sand[1] == ground + 1:
                if not part2:
                    return dropped_sand
                grid.add(sand)
                break
        dropped_sand += 1
        # part 2 answer
        if sand == (500, 0):
            return dropped_sand


if __name__ == '__main__':
    print(f'part 1: {main()}')
    print(f'part 2: {main(True)}')
