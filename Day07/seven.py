import re
from collections import defaultdict


def parse_bag_rule(line):
  pattern = '^(\\w+ \\w+) bags contain (no other bags|.+).$'
  matches = re.match(pattern, line)
  outer_colour = matches.group(1)
  inner_bags = matches.group(2)
  if inner_bags == 'no other bags':
    return outer_colour, []
  else:
    splits = inner_bags.split(', ')
    pattern = '^(\\d+) (\w+ \w+) bags?$'
    inner_list = []
    for s in splits:
      matches = re.search(pattern, s)
      inner_list.append((int(matches.group(1)), matches.group(2)))
    return outer_colour, inner_list
  

def build_direct_outer_bags():
  outer_bags_map = defaultdict(list)
  with open('seven_input.txt', 'r') as file:
    line = file.readline().strip()
    while line:
      outer_colour, inner_list = parse_bag_rule(line)
      for _, c in inner_list:
        bag_list = outer_bags_map[c]
        bag_list.append(outer_colour)
        outer_bags_map[c] = bag_list
      line = file.readline().strip()
  return outer_bags_map


def build_direct_inner_bags():
  inner_bags_map = defaultdict(list)
  with open('seven_input.txt', 'r') as file:
    line = file.readline().strip()
    while line:
      outer_colour, inner_list = parse_bag_rule(line)
      inner_bags_map[outer_colour] = inner_list
      line = file.readline().strip()
  return inner_bags_map


def count_outermost_colours(colour):
  outer_bags_map = build_direct_outer_bags()
  bags_set = set()
  bags = [colour]
  while bags:
    c = bags.pop()
    outer_c = set(outer_bags_map[c])
    bags.extend(outer_c.difference(bags_set))
    bags_set = bags_set.union(outer_c)
  print(f"The number of bag colours containing {colour} is {len(bags_set)}\n")
  print(f"The colours containing {colour} are {bags_set}")


def count_inner_bags_aux(inner_bags_map, freq, colour):
  count = 0
  for f, c in inner_bags_map[colour]:
    count += count_inner_bags_aux(inner_bags_map, f, c)
  return freq * (1 + count)
  

def count_individual_inner_bags(colour):
  inner_bags_map = build_direct_inner_bags()
  count = count_inner_bags_aux(inner_bags_map, 1, colour) - 1
  print(f"The {colour} bag contains {count} other bags")


count_individual_inner_bags('shiny gold')