PREDICTED = {'A': 'Rock', "B": "Paper", "C": 'Scissors'}
RESPONSE = {'X': 'Rock', "Y": "Paper", "Z": 'Scissors'}
POINTS = {"Rock": 1, "Paper": 2, "Scissors": 3}
WIN = [('Scissors', 'Rock'), ('Rock', 'Paper'), ('Paper', 'Scissors')]
LOSE = {v: k for k, v in WIN}
WIN2 = {v: k for v, k in WIN}


def main():
    with open('day2.txt') as f:
        data = [line.rstrip('\n') for line in f]
    score = 0
    for hand in data:
        elf, player = hand.split()
        score += POINTS.get(RESPONSE.get(player))
        if (PREDICTED.get(elf), RESPONSE.get(player)) in WIN:
            score += 6
        elif PREDICTED.get(elf) == RESPONSE.get(player):
            score += 3
    print(f'part 1: {score}')

    # part 2
    result = 0
    for hand in data:
        elf, player = hand.split()
        match player:
            case 'X':
                result += POINTS.get(LOSE.get(PREDICTED.get(elf)))
            case 'Y':
                result += POINTS.get(PREDICTED.get(elf)) + 3
            case 'Z':
                result += POINTS.get(WIN2.get(PREDICTED.get(elf))) + 6
    print(f'part 2: {result}')


if __name__ == '__main__':
    main()
