def main():
    with open('day3.txt') as f:
        data = [line.rstrip('\n') for line in f]
    result1 = 0
    for bag in data:
        items1 = bag[:len(bag) // 2]
        items2 = bag[len(bag) // 2:]
        set_items1 = set(char for char in items1)
        set_items2 = set(char for char in items2)
        union = str(list(set_items1 & set_items2)[0])
        if union.isupper():
            result1 += ord(union) - 38
        else:
            result1 += ord(union) - 96
    print(f"part 1: {result1}")

    result2 = 0
    for i in range(0, len(data) - 2, 3):
        bag1 = data[i]
        bag2 = data[i + 1]
        bag3 = data[i + 2]
        set_bag1 = set(char for char in bag1)
        set_bag2 = set(char for char in bag2)
        set_bag3 = set(char for char in bag3)
        bag_union = str(list(set_bag1 & set_bag2 & set_bag3)[0])
        if bag_union.isupper():
            result2 += ord(bag_union) - 38
        else:
            result2 += ord(bag_union) - 96
    print(f'part 2: {result2}')


if __name__ == '__main__':
    main()
