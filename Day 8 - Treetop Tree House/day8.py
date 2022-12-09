import numpy


def is_outer(row_size: int, col_size: int, row: int, col: int) -> bool:
    return row - 1 < 0 or row + 1 == row_size or col - 1 < 0 or col + 1 == col_size


def is_visible(main_tree: int, nearby_trees: [int]) -> bool:
    for trees in nearby_trees:
        if main_tree > max(trees):
            return True
    return False


def main():
    with open('day8.txt') as f:
        data = [line.rstrip('\n') for line in f]
    forest = numpy.array([list(map(int, line)) for line in data])
    row_size = len(forest[0])
    col_size = len(forest)
    visible_trees = 0
    scenic_scores = []

    # loop through forest
    for row in range(row_size):
        for col in range(col_size):
            if is_outer(row_size, col_size, row, col):
                visible_trees += 1
            else:
                # interior trees
                main_tree = forest[row][col]
                top = forest[:row, col][::-1]
                bot = forest[row + 1:, col]
                left = forest[row, :col][::-1]
                right = forest[row, col + 1:]
                nearby_trees = [top, left, bot, right]
                if is_visible(main_tree, nearby_trees):
                    visible_trees += 1

                # part 2
                scenic_scores.append(get_view(main_tree, nearby_trees))
    print(f"part 1: {visible_trees}")
    print(f"part 2: {max(scenic_scores)}")


def get_view(main_tree: int, other_trees: [int]) -> []:
    views = []
    for trees in other_trees:
        distance = 0
        for tree in trees:
            distance += 1
            if main_tree <= tree:
                break
        views.append(distance)
    return numpy.prod(views)


if __name__ == '__main__':
    main()
