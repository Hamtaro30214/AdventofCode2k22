class Catalog:
    def __init__(self, name, parent=None):
        self.name = name
        self.parent = parent
        self.catalogs = []
        self.files = []

    def get_file_size(self):
        return sum(file.size for file in self.files)

    def get_catalog_size(self):
        return sum(catalog.get_size() for catalog in self.catalogs)

    def get_size(self):
        if not self.catalogs:
            return self.get_file_size()
        return self.get_file_size() + self.get_catalog_size()

    def get_catalog_by_name(self, catalog_name):
        for catalog in self.catalogs:
            if catalog.name == catalog_name:
                return catalog


class File:
    def __init__(self, name, size):
        self.name = name
        self.size = size


def main():
    with open("day7.txt", 'r') as f:
        data = f.read().splitlines()[2:]

    root_catalog = current_catalog = Catalog('/')

    for elf in data:
        elf_after_split = elf.split()
        if elf_after_split[0] == 'dir':
            current_catalog.catalogs.append(Catalog(elf_after_split[1], current_catalog))
        if elf_after_split[1] == 'cd':
            if elf_after_split[2] == '..':
                current_catalog = current_catalog.parent
            else:
                current_catalog = current_catalog.get_catalog_by_name(elf_after_split[2])
        if elf_after_split[0].isdigit():
            current_catalog.files.append(File(elf_after_split[1], int(elf_after_split[0])))

    global result1
    result1 = 0
    count_size(root_catalog)
    print(f'part 1: {result1}')

    global result2
    result2 = []
    unused_space = 70000000 - root_catalog.get_size()
    find_folder_to_delete(unused_space, root_catalog)
    print(f'part 2: {min(result2)}')


def find_folder_to_delete(unused_space, node):
    global result2
    for child in node.catalogs:
        released_space = child.get_size() + unused_space
        if released_space >= 30000000:
            result2.append(child.get_size())
        find_folder_to_delete(unused_space, child)


def count_size(node):
    global result1
    for child in node.catalogs:
        if child.get_size() <= 100000:
            result1 += child.get_size()
        count_size(child)


if __name__ == '__main__':
    main()
