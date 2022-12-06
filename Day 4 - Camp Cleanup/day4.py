def main():
    with open('day4.txt') as f:
        data = [line.rstrip('\n') for line in f]

    result1 = 0
    result2 = 0
    for sections in data:
        pair1, pair2 = sections.split(',')
        first_pair = list(map(int, pair1.split('-')))
        second_pair = list(map(int, pair2.split('-')))
        if first_pair[1] - first_pair[0] >= second_pair[1] - second_pair[0]:
            if first_pair[0] <= second_pair[0] and first_pair[1] >= second_pair[1]:
                result1 += 1
        else:
            if second_pair[0] <= first_pair[0] and second_pair[1] >= first_pair[1]:
                result1 += 1

        pair_set1 = set(range(first_pair[0], first_pair[1] + 1))
        pair_set2 = set(range(second_pair[0], second_pair[1] + 1))
        if not pair_set1.isdisjoint(pair_set2):
            result2 += 1
    print(f'part 1: {result1}')
    print(f'part 2: {result2}')


if __name__ == '__main__':
    main()
