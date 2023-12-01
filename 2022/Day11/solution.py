from collections import deque

import math
import numpy as np
import utils

MODULO = 0


class Monkey:
    def __init__(self, worry_func, test_value, monkey_true, monkey_false, items):
        if MODULO:
            self.worry_func = lambda x: worry_func(x) % MODULO
        else:
            self.worry_func = lambda x: math.floor(worry_func(x) / 3)
        self.test_value = test_value
        self.monkey_true = monkey_true
        self.monkey_false = monkey_false
        self.items = deque(items)
        self.inspected_count = 0

    def inspect(self, monkeys):
        while len(self.items) != 0:
            item = self.items.popleft()
            item = self.worry_func(item)
            if item % self.test_value == 0:
                monkeys[self.monkey_true].catch_item(item)
            else:
                monkeys[self.monkey_false].catch_item(item)
            self.inspected_count += 1

    def catch_item(self, item):
        self.items.append(item)


def construct_worry_lvl_func(line: str):
    op_map = {
        '+': (lambda x1, x2: x1 + x2),
        '*': (lambda x1, x2: x1 * x2),
    }
    p1, op, p2 = line.split('= ')[1].split(' ')
    if p1 == p2:
        return lambda x: op_map[op](x, x)
    else:
        return lambda x: op_map[op](x, int(p2))


def create_monkey(monkey: str):
    monkey = monkey.split('\n')
    items = utils.int_list(monkey[1].split(': ')[-1], ', ')
    worry_func = construct_worry_lvl_func(monkey[2])
    test_value = int(monkey[3].split(' ')[-1])
    monkey_true = int(monkey[4][-1])
    monkey_false = int(monkey[5][-1])
    return Monkey(worry_func, test_value, monkey_true, monkey_false, items)


def process_data(lines: str):
    monkeys = lines.split('\n\n')
    return list(map(create_monkey, monkeys))


def calculate_monkey_business_level(monkeys: list[Monkey], rounds_num: int):
    for i in range(rounds_num):
        for monkey in monkeys:
            monkey.inspect(monkeys)
        # print_monkeys(monkeys)

    active_monkeys = sorted(monkeys, key=lambda m: m.inspected_count, reverse=True)
    return active_monkeys[0].inspected_count * active_monkeys[1].inspected_count


def print_monkeys(monkeys: list[Monkey]):
    for i, monk in enumerate(monkeys):
        items = ', '.join(np.array(list(monk.items)).astype(str))
        print("Monkey {}: {}".format(i, items))


if __name__ == "__main__":
    mnks = utils.read_whole_file(process_data)
    business_lvl = calculate_monkey_business_level(mnks, 20)
    print("Part 1: The level of monkey business is {}".format(business_lvl))

    MODULO = math.prod(map(lambda m: m.test_value, mnks))
    mnks = utils.read_whole_file(process_data)
    business_lvl = calculate_monkey_business_level(mnks, 10000)
    print("Part 2: The level of monkey business is {}".format(business_lvl))
