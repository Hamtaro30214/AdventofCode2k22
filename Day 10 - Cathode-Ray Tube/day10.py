class CRT:
    def __init__(self):
        self.cycle = 0
        self.register = 1
        self.cycle_limit = list(range(20, 221, 40))
        self.signal_strengths = 0
        self.get_input()

    def get_input(self):
        with open('day10.txt') as f:
            self.data = [line.rstrip('\n') for line in f]

    def part1(self):
        for instruction in self.data:
            instruction = instruction.split()
            self.cycle += 1
            if self.cycle in self.cycle_limit:
                self.signal_strengths += self.cycle * self.register
            if len(instruction) == 2:
                self.cycle += 1
                if self.cycle in self.cycle_limit:
                    self.signal_strengths += self.cycle * self.register
                self.register += int(instruction[1])
        print(self.signal_strengths)

    def update_sprite_limit(self):
        self.sprite_limit = list(range(self.position_of_sprite, self.position_of_sprite + 3))

    def check_sprite_length(self):
        if len(self.sprite) == 40:
            self.cycle = -1
            self.crt_display.append(self.sprite)
            self.sprite = ''

    def update_sprite(self):
        char = '.'
        if self.cycle in self.sprite_limit:
            char = '#'
        self.sprite += char
        self.check_sprite_length()

    def default_variables(self):
        self.cycle = -1
        self.position_of_sprite = 0
        self.sprite_limit = [0, 1, 2]
        self.sprite = ''
        self.crt_display = []

    def part2(self):
        self.default_variables()
        for instruction in self.data:
            instruction = instruction.split()
            self.cycle += 1
            self.update_sprite()
            if len(instruction) == 2:
                self.cycle += 1
                self.update_sprite()
                self.position_of_sprite += int(instruction[1])
                self.update_sprite_limit()

        for sprite in self.crt_display:
            print(sprite)


def main():
    kineskop = CRT()
    kineskop.part1()
    kineskop.part2()


if __name__ == '__main__':
    main()
