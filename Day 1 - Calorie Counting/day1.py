def main():
    with open('day1.txt') as f:
        data = [line.rstrip('\n') for line in f]
    elfs = []
    calories = 0
    for food in data:
        if food:
            calories += int(food)
        else:
            elfs.append(calories)
            calories = 0
    elfs.append(calories)
    print(f'part 1: {max(elfs)}')

    # part 2
    top_three = []
    for _ in range(3):
        top_three.append(max(elfs))
        elfs.remove(max(elfs))
    print(f'part 2: {sum(top_three)}')


if __name__ == '__main__':
    main()
