import numpy as np
import utils


class Node:
    def __init__(self, name: str, is_file: bool, parent, size: int):
        self.name = name
        self.is_file = is_file
        self.sub_nodes = {}
        self.parent = parent
        self.size = size

    def get_size(self):
        if self.size == 0:
            self.size = sum([n.get_size() for n in self.sub_nodes.values()])
        return self.size

    def get_sizes_of_filtered_nodes(self, predicate_func) -> np.ndarray:
        filtered_nodes = np.array([])
        for n in self.sub_nodes.values():
            filtered_nodes = np.append(filtered_nodes, n.get_sizes_of_filtered_nodes(predicate_func))

        if predicate_func(self):
            filtered_nodes = np.append(filtered_nodes, self.size)

        return filtered_nodes


def build_directory(terminal: list[str]) -> Node:
    root = Node("/", is_file=False, parent=None, size=0)
    curr_node = root

    for line in terminal:
        if line == "$ cd /":
            curr_node = root
        elif line == "$ cd ..":
            curr_node = curr_node.parent
        elif line.startswith("$ cd"):
            _, _, dir_name = line.split(' ')
            curr_node = curr_node.sub_nodes[dir_name]
        elif line.startswith("$ ls"):
            continue
        elif line.startswith("dir"):
            _, dir_name = line.split(' ')
            if dir_name not in curr_node.sub_nodes.keys():
                curr_node.sub_nodes[dir_name] = Node(dir_name, is_file=False, parent=curr_node, size=0)
        else:
            size, filename = line.split(' ')
            curr_node.sub_nodes[filename] = Node(filename, is_file=True, parent=curr_node, size=int(size))

    return root


def calculate_dir_sum(root: Node):
    predicate_func = lambda n: not n.is_file and n.get_size() <= 100000
    filtered_nodes = root.get_sizes_of_filtered_nodes(predicate_func)
    return sum(filtered_nodes)


def find_dir_to_delete(root: Node):
    needed_space = 30000000
    free_space = 70000000 - root.get_size()
    to_free = needed_space - free_space
    is_dir_candidate = lambda n: not n.is_file and n.get_size() >= to_free
    filtered_dirs = root.get_sizes_of_filtered_nodes(is_dir_candidate)
    return min(filtered_dirs)


if __name__ == "__main__":
    directory = build_directory(utils.read_input_file())
    total = calculate_dir_sum(directory)
    print("Part 1: The sum of the total sizes of the directories is {}".format(total))
    smallest_candidate_dir = find_dir_to_delete(directory)
    print("Part 2: The size of the smallest directory to delete is {}".format(smallest_candidate_dir))
