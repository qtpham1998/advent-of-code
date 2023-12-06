from collections import deque
import re
import numpy as np
import sys
import utils


class Mapping:
    def __init__(self, map_defs: str):
        categories, ranges = map_defs.strip().split(" map:\n")
        self.src_category, _, self.dst_category = categories.split("-")
        self.ranges = self.parse_ranges(ranges)

    def parse_ranges(self, ranges: str) -> list[tuple[int, int, int]]:
        mappings = []
        for line in ranges.split("\n"):
            dst_start, src_start, length = line.strip().split()
            mappings.append((int(dst_start), int(src_start), int(length)))

        return mappings

    def get_destination_ranges(self, src: list[tuple[int, int]]) -> list[tuple]:
        destinations = []

        for dst_start, src_start, length in self.ranges:
            new_src = []

            for s_start, s_len in src:
                s_end = s_start + s_len
                src_end = src_start + length
                # No intersection with mapping
                if s_start >= src_end or s_end < src_start:
                    new_src.append((s_start, s_len))
                else:
                    d_start = dst_start + max(src_start, s_start) - src_start
                    d_len = min(src_end, s_end) - max(src_start, s_start)
                    destinations.append((d_start, d_len))

                    # Append leftover range not applicable to this mapping
                    if s_start < src_start:
                        new_src.append((s_start, src_start - s_start))

                    if s_end >= src_end:
                        new_src.append((src_end, s_end - src_end + 1))

            src = new_src

        return destinations + src


def get_seed_sources(seeds: str) -> list[tuple]:
    seeds = utils.number_list(seeds.split(":")[1], num_type=np.longlong)
    return [(s, 1) for s in seeds]


def get_seed_ranges(seeds: str) -> np.ndarray:
    seeds = seeds.split(":")[1].strip()
    seed_ranges = []
    for g in re.finditer("(\\d+) (\\d+)", seeds):
        seed_ranges.append((np.longlong(g.group(1)), np.longlong(g.group(2))))
    return np.array(seed_ranges, dtype=object)


def process_data(inp: str) -> (list[int], list[tuple], dict[str, Mapping]):
    seeds_line, *map_defs = inp.split("\n\n")
    seeds_one = get_seed_sources(seeds_line)
    seeds_ranges = get_seed_ranges(seeds_line)
    maps = {}
    for m in map_defs:
        mapping = Mapping(m)
        maps[mapping.src_category] = mapping

    return seeds_one, seeds_ranges, maps


def find_lowest_location(seeds: list[tuple[int, int]], maps: dict[str, Mapping]) -> int:
    min_location = sys.maxsize

    for s in seeds:
        key = "seed"
        src = [s]

        while key in maps.keys():
            mapping = maps[key]
            src = mapping.get_destination_ranges(src)
            key = mapping.dst_category

        src.sort(key=lambda k: k[0])
        min_location = min(min_location, src[0][0])

    return min_location


if __name__ == '__main__':
    seeds_one, seeds_ranges, maps = utils.read_whole_file(process_data)
    lowest_location = find_lowest_location(seeds_one, maps)
    print("Part 1: The lowest seed location is {}".format(lowest_location))

    lowest_location = find_lowest_location(seeds_ranges, maps)
    print("Part 2: The lowest seed location is {}".format(lowest_location))


