from utils.api import get_input
from collections import deque


class Directory:
    def __init__(self, parent=None):
        self.parent = parent
        self.children = {}
        self.size_memo = None

    def add(self, key, child):
        self.children[key] = child

    def get(self, key):
        return self.children[key]

    def size(self):
        if not self.children:
            return 0
        if self.size_memo is None:
            map_thing = map(lambda x: x.size(), self.children.values())
            self.size_memo = sum(map_thing)
        return self.size_memo


class File:
    def __init__(self, size):
        self.sz = size

    def size(self):
        return self.sz


input_str = get_input(7)

root = Directory()
current_directory = None

pos = 0
lines = input_str.split("\n")
line_count = len(lines)
while pos < line_count:
    line = lines[pos]
    pos += 1
    if not line.startswith("$"):
        print("???")
        exit()

    cmd = line.split(" ")[1:]
    if cmd[0] == "ls":
        while pos < line_count and not lines[pos].startswith("$"):
            a, b = lines[pos].split(" ")
            pos += 1
            if a == "dir":
                current_directory.add(b, Directory(current_directory))
            else:
                current_directory.add(b, File(int(a)))
    elif cmd[0] == "cd":
        path = cmd[1]
        if path == "/":
            current_directory = root
        elif path == "..":
            current_directory = current_directory.parent
        else:
            current_directory = current_directory.get(path)


leaf_dirs = deque()
all_dirs = []
queue = deque()
queue.append(root)
while len(queue) > 0:
    node = queue.popleft()
    had_children = False
    for child in node.children.values():
        if isinstance(child, Directory):
            all_dirs.append(child)
            queue.append(child)
            had_children = True

    if not had_children:
        leaf_dirs.append(node)

sum_one = 0
seen_dirs = set()
# first idea failed... could just traverse upwards instead of using another queue
while leaf_dirs:
    leaf_dir = leaf_dirs.popleft()
    if leaf_dir in seen_dirs:
        continue
    else:
        seen_dirs.add(leaf_dir)
    size = leaf_dir.size()
    if size <= 100000:
        sum_one += size
        leaf_dirs.append(leaf_dir.parent)

total_disk_space = 70000000
free_space_required = 30000000
used_space = root.size()
delete_amount = free_space_required - (total_disk_space - used_space)
smallest_to_delete = None
for dir in all_dirs:
    if dir.size() >= delete_amount:
        if not smallest_to_delete:
            smallest_to_delete = dir
        elif smallest_to_delete.size() > dir.size():
            smallest_to_delete = dir

print(sum_one)
print(smallest_to_delete.size())
