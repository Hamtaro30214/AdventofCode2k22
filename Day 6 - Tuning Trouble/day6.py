def solve(limit):
    with open('day6.txt') as f:
        data = f.readline()
    step = limit
    for line_id in range(len(data) - limit - 1):
        increase = 0
        chars = []
        for _ in range(limit):
            chars.append(data[line_id + increase])
            increase += 1
        if len(set(chars)) == limit:
            return step
        step += 1


if __name__ == '__main__':
    print(f'part 1: {solve(4)}')
    print(f'part 2: {solve(14)}')
