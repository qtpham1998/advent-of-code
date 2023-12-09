import math
import re
import utils


def process_nodes(inp: str) -> (dict[str, (str, str)], list[str]):
    network = {}
    starting_nodes = []

    for match in re.finditer("([A-Z]{3}) = \(([A-Z]{3}), ([A-Z]{3})\)", inp):
        node = match.group(1)
        network[node] = (match.group(2), match.group(3))

        if node[-1] == "A":
            starting_nodes.append(node)

    return network, starting_nodes


def process_data(inp: str) -> (str, dict[str, (str, str)], list[str]):
    instr, network = inp.split("\n\n")
    return instr, *process_nodes(network)


def count_steps_to_dest(instr: str, network: dict[str, (str, str)]) -> int:
    steps = 0
    curr_node = "AAA"
    while curr_node != "ZZZ":
        left, right = network[curr_node]
        curr_node = left if instr[steps % len(instr)] == "L" else right
        steps += 1
    return steps


def count_steps_to_destinations(instr: str, network: dict[str, (str, str)], starting_nodes: list[str]) -> int:
    steps_to_dest = []
    for s_node in starting_nodes:
        steps = 0
        while s_node[-1] != "Z":
            left, right = network[s_node]
            s_node = left if instr[steps % len(instr)] == "L" else right
            steps += 1
        steps_to_dest.append(steps)
    return math.lcm(*steps_to_dest)


if __name__ == '__main__':
    instr, network, starting_nodes = utils.read_whole_file(process_data)
    steps = count_steps_to_dest(instr, network)
    print("Part 1: The number of steps to reach ZZZ is {}".format(steps))
    steps = count_steps_to_destinations(instr, network, starting_nodes)
    print("Part 2: The number of steps to reach **Z is {}".format(steps))
