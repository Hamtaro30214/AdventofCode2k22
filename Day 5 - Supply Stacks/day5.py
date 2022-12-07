def create_crates(crates: []) -> []:
    start = 1
    stacked_crates = []
    while start < len(crates[0]):
        table = []
        for i in range(8):
            table.append(crates[i][start])
        stacked_crates.append([i for i in table[::-1] if i.isupper()])
        start += 4
    return stacked_crates


def main():
    with open('day5.txt') as f:
        data = [line.rstrip('\n') for line in f]
    result1 = ''
    result2 = ''
    crates = data[:10]
    commands = data[10:]
    stacked_crates = create_crates(crates)
    crane_crates = create_crates(crates)

    for command in commands:
        command = command.split()
        amount = int(command[1])
        removed_create = int(command[3])
        updated_create = int(command[5])
        help_tab = []
        for _ in range(amount):
            # part1
            crane_crates[updated_create - 1].append(crane_crates[removed_create - 1].pop())
            # part 2
            help_tab.append(stacked_crates[removed_create - 1].pop())
        # part 2
        stacked_crates[updated_create - 1].extend(help_tab[::-1])

    for crate in crane_crates:
        result1 += crate[-1]
    print(f'part 1: {result1}')
    for crate in stacked_crates:
        result2 += crate[-1]
    print(f'part 2: {result2}')


if __name__ == '__main__':
    main()
