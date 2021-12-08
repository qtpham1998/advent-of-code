from typing import Dict

import numpy as np
import utils


def get_length_dict(patterns):
    p_dicts = {}
    for p in patterns:
        if len(p) in p_dicts.keys():
            p_dicts[len(p)].append(set(p))
        else:
            p_dicts[len(p)] = [set(p)]
    return p_dicts


def pre_process_data(line: str) -> (np.ndarray, Dict):
    patterns = line.split(' | ')
    outputs = utils.map_list(set, patterns[1].split())
    patterns = get_length_dict(patterns[0].split())
    return patterns, outputs


def get_data() -> np.ndarray:
    return utils.read_input_file(pre_process_data)


def is_unique_segments_digit(output: str) -> bool:
    return len(output) in [2, 3, 4, 7]


def count_unique_digits(data: np.ndarray) -> int:
    outputs = utils.map_list(lambda d: d[1], data).flatten()
    count = 0
    for output in outputs:
        if len(output) in [2, 3, 4, 7]:
            count += 1
    return count


def decipher_connections(patterns: Dict[int, np.ndarray]) -> Dict:
    connections = {
        1: patterns[2][0],
        4: patterns[4][0],
        7: patterns[3][0],
        8: patterns[7][0],
    }

    for p in patterns[6]:
        if p.issuperset(connections[4]):
            connections[9] = p
        elif p.issuperset(connections[1]):
            connections[0] = p
        else:
            connections[6] = p

    for p in patterns[5]:
        if p.issuperset(connections[7]):
            connections[3] = p
        elif p.issubset(connections[9]):
            connections[5] = p
        else:
            connections[2] = p

    return connections


def get_output_value(outputs: np.ndarray, connections: dict) -> int:
    output_values = []
    for output in outputs:
        for val, cons in connections.items():
            if output == cons:
                output_values.append(str(val))
                break

    output_values = "".join(output_values)
    return int(output_values)


def count_total_output(data: np.ndarray) -> int:
    total = 0
    for p, o in data:
        connections = decipher_connections(p)
        total += get_output_value(o, connections)
    return total


def main():
    count = count_unique_digits(get_data())
    print("The digits 1, 4, 7, or 8 appear {} times.".format(count))
    count = count_total_output(get_data())
    print("The total of ouputs is {}".format(count))


if __name__ == '__main__':
    main()