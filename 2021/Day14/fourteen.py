from collections import defaultdict, Counter

import utils


def pre_process_rules(rules: str) -> defaultdict:
    rules_dict = defaultdict(lambda: "")
    for rule in rules.split('\n'):
        rule = rule.split(' -> ')
        rules_dict[rule[0]] = rule[1]
    return rules_dict


def get_data() -> tuple:
    data = utils.read_whole_file().split('\n\n')
    template = data[0]
    rules = pre_process_rules(data[1])
    return template, rules


def run_step(polymer: str, rules: defaultdict) -> str:
    new_poly = [polymer[0]]
    for i in range(len(polymer) - 1):
        key = polymer[i:i+2]
        new_poly.append(rules[key])
        new_poly.append(polymer[i+1])
    return ''.join(new_poly)


def dynamic_process_polymer(polymer: str, rules: defaultdict, memory: defaultdict, steps) -> Counter:
    elem_count = Counter()

    for i in range(len(polymer) - 1):
        section = polymer[i:i+2]

        if steps in memory[section]:
            elem_count.update(memory[section][steps])

        elif steps == 0:
            memory[section][0] = Counter(section[:-1])
            elem_count.update(memory[section][0])

        else:
            next_poly = run_step(section, rules)
            count = dynamic_process_polymer(next_poly, rules, memory, steps - 1)
            memory[section][steps] = count
            elem_count.update(count)

    return elem_count


def get_count_diff(polymer: str, rules: defaultdict, steps: int) -> int:
    memory = defaultdict(lambda: {})
    elem_count = dynamic_process_polymer(polymer, rules, memory, steps)
    elem_count.update(polymer[-1])
    return max(elem_count.values()) - min(elem_count.values())


def main():
    steps = 40
    diff = get_count_diff(*get_data(), steps)
    print("The most common element count take away the least common element count is {}".format(diff))


if __name__ == '__main__':
    main()
