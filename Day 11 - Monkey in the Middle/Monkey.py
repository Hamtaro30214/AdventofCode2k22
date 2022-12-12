class Monkey:
    def __init__(self, number, items: [], operation: str, divisible: int, test: [], inspected_items=0):
        self.number = number
        self.items = items
        self.operation = operation
        self.divisible = divisible
        self.test = test
        self.inspected_items = inspected_items

    def __iter__(self):
        self.variables_left = 0
        return self

    def __next__(self):
        self.variables_left += 1
        match self.variables_left:
            case 1:
                return self.number
            case 2:
                return ' '.join(str(v).strip() for v in self.items)
            case 3:
                return self.operation
            case 4:
                return self.divisible
            case 5:
                return ' '.join(str(v).strip() for v in self.test)
            case 6:
                return self.inspected_items
            case _:
                raise StopIteration

    def __eq__(self, other):
        return all((
            self.number == other.number,
            self.items == other.items,
            self.operation == other.operation,
            self.divisible == other.divisible,
            self.test == other.test,
            self.inspected_items == other.inspected_items
        ))

    def __str__(self):
        return f"{self.number}, {self.items}, {self.operation}, {self.divisible}, {self.test}, {self.inspected_items}"

    def __repr__(self):
        return self.__str__()
