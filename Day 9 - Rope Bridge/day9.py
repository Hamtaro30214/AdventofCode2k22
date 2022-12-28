import math


class Rope:
    def __init__(self, horizontal, vertical):
        self.horizontal = horizontal
        self.vertical = vertical

    def __eq__(self, other):
        return self.horizontal == other.horizontal and self.vertical == other.vertical

    def __add__(self, other):
        return Rope(self.horizontal + other.horizontal, self.vertical + other.vertical)

    def __sub__(self, other):
        return Rope(self.horizontal - other.horizontal, self.vertical - other.vertical)

    def __str__(self):
        return f"{self.horizontal},{self.vertical}"

    def __repr__(self):
        return self.__str__()

    def __hash__(self):
        return hash((self.horizontal, self.vertical))

    def __iter__(self):
        return iter((self.horizontal, self.vertical))


MOTIONS = {'U': Rope(-1, 0), "D": Rope(1, 0), "L": Rope(0, -1), "R": Rope(0, 1)}


def main(number_of_knots: int):
    with open('day9.txt') as f:
        data = [line.rstrip('\n') for line in f]
    knots = [Rope(0, 0)] * number_of_knots
    visited = set()
    for command in data:
        move_type, move_amount = command.split()
        for _ in range(int(move_amount)):
            knots[0] += MOTIONS.get(move_type)
            for index in range(1, len(knots)):
                diff_rope = knots[index - 1] - knots[index]
                if abs(diff_rope.horizontal) > 1 or abs(diff_rope.vertical) > 1:
                    new_horizontal = knots[index].horizontal
                    new_vertical = knots[index].vertical
                    if diff_rope.horizontal:
                        new_horizontal = knots[index].horizontal + int(math.copysign(1, diff_rope.horizontal))
                    if diff_rope.vertical:
                        new_vertical = knots[index].vertical + int(math.copysign(1, diff_rope.vertical))
                    knots[index] = Rope(new_horizontal, new_vertical)
            visited.add(knots[-1])
    return len(visited)


if __name__ == '__main__':
    print(main(2))
    print(main(10))
