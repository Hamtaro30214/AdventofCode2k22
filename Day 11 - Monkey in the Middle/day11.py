import math
from Monkey import Monkey


def create_monkeys() -> []:
    with open('day11.txt') as f:
        data = [line.rstrip('\n') for line in f]

    monkey_number = -1
    info_amount = 5
    monkeys = []
    monkeys_items = []
    next_monkey = []

    for decision in data:
        if len(decision) == 0:
            info_amount = 5
            monkeys.append(Monkey(monkey_number, *monkeys_items))
            next_monkey.clear()
            monkeys_items.clear()
        elif len(decision.split()) == 2:
            monkey_number += 1
        else:
            match info_amount:
                case 5:
                    decision = decision.split(':')[-1]
                    items = [int(item.strip()) for item in decision.split(',')]
                    monkeys_items.append(items)
                case 4:
                    operation = decision.split(':')[-1].strip()
                    operations = operation.split('=')[-1].strip().split()
                    new_operation = []
                    for oper in operations:
                        if oper == 'old':
                            oper = '{' + oper + '}'
                        new_operation.append(oper)
                    new_operation = ' '.join(new_operation)
                    monkeys_items.append(new_operation)
                case 3:
                    divisible = int(decision.split()[-1])
                    monkeys_items.append(divisible)
                case 2:
                    dec = int(decision.split()[-1])
                    next_monkey.append(dec)
                case 1:
                    dec = int(decision.split()[-1])
                    next_monkey.append(dec)
                    monkeys_items.append(next_monkey.copy())
            info_amount -= 1
    monkeys.append(Monkey(monkey_number, *monkeys_items))
    return monkeys


def main(rounds=20, user_worry_level=True):
    monkeys = create_monkeys()
    factors = math.prod(m.divisible for m in monkeys)

    for i in range(rounds):
        for monkey in monkeys:
            monkey.inspected_items += len(monkey.items)
            for item in monkey.items:
                worry_level = eval(monkey.operation.format(old=item))
                if user_worry_level:
                    worry_level = worry_level // 3
                else:
                    worry_level = worry_level % factors
                if worry_level % monkey.divisible == 0:
                    recipient_monkey = monkeys[monkey.test[0]]
                else:
                    recipient_monkey = monkeys[monkey.test[1]]
                recipient_monkey.items.append(worry_level)
            monkey.items.clear()
    monkey1, monkey2 = sorted(monkey.inspected_items for monkey in monkeys)[-2:]
    return monkey1 * monkey2


if __name__ == '__main__':
    print(f'part 1: {main()}')
    print(f'part 2: {main(rounds=10000, user_worry_level=False)}')
