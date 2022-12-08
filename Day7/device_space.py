TOTAL_DISK_SPACE = 70000000
LEAST_NEEDED_SPACE = 30000000

class Directory:
    def __init__(self, name):
        self.name = name
        self.size = 0
        self.files = []
        self.previous = None
        self.subdirs = []

    def add_file(self, file):
        self.files.append(file)
        self.size += file.size

    def add_subdir(self, subdir):
        self.subdirs.append(subdir)

    def get_total_size(self):
        # Return the total size of all subdirs
        total_size = self.size
        for subdir in self.subdirs:
            total_size += subdir.get_total_size()
        return total_size

    def __repr__(self):
        return f"Dir {self.name} : {self.get_total_size()}"

class File:
    def __init__(self, name, size):
        self.name = name
        self.size = size

    def __repr__(self):
        return f"File :{self.name}, {self.size}"

def parse_data(data):
    root = Directory("/")
    current_dir = root
    for line in data:
        splitted = line.split(" ")
        if line.startswith("dir"):
            new_dir = Directory(splitted[1])
            current_dir.add_subdir(new_dir)
            new_dir.previous = current_dir
        elif splitted[0].isdigit():
            current_dir.add_file(File(splitted[1], int(splitted[0])))
        elif line == "cd ..":
            current_dir = current_dir.previous
        elif splitted[0] == "cd":
            for subdir in current_dir.subdirs:
                if subdir.name == splitted[1]:
                    current_dir = subdir
    return root

with open("input.txt", "r") as file:
    data = [l.replace("$ ","") for l in file.read().splitlines()]
root = parse_data(data)

# Get directory by size 
def get_dir_by_size(root, size, operation):
    dirs = []
    for subdir in root.subdirs:
        if operation == "<=" and subdir.get_total_size() <= size:
            dirs.append(subdir)
        elif operation == ">=" and subdir.get_total_size() >= size:
            dirs.append(subdir)
        dirs += get_dir_by_size(subdir, size, operation)
    return sorted(dirs, key=lambda x: x.get_total_size(), reverse=True)

small_dirs = get_dir_by_size(root, 100000, "<=")
print(f"Part 1: {sum([d.get_total_size() for d in small_dirs])}")

CURRENT_SPACE = TOTAL_DISK_SPACE - root.get_total_size()
NEEDED_SPACE = LEAST_NEEDED_SPACE - CURRENT_SPACE
big_dirs = get_dir_by_size(root,NEEDED_SPACE, ">=")
print(f"Part 2: {min([d.get_total_size() for d in big_dirs])}")

# Bonus !
def print_tree(root, level=0):
    print("-" * level + str(root))
    for subdir in root.subdirs:
        print_tree(subdir, level + 1)
# print_tree(root)