from collections import defaultdict


def parse_file():
  with open('ten_input.txt', 'r') as file:
    lines = file.read().strip().split('\n')
    lines = list(map(lambda x: int(x), lines))
    return [0] + sorted(lines)


def find_jolt_differences():
  adapters = parse_file()
  differences = defaultdict(lambda: 0)
  for i, num1 in enumerate(adapters):
    if i == len(adapters) - 1:
      differences[3] += 1
      return differences
    num2 = adapters[i + 1]
    differences[num2 - num1] += 1
  return differences


def calculate_arrangements(adapters, arr_map, index):
  adapter_output = adapters[index]
  if adapter_output in arr_map:
    return arr_map
  else:
    for i in range(1, min(4, len(adapters) - index)):
      next_adapter = adapters[index + i]
      if next_adapter - adapter_output > 3: break
      arr_map = calculate_arrangements(adapters, arr_map, index + i)
      arr_map[adapter_output] += arr_map[next_adapter]
    return arr_map
  

def calculate_adapters_arr_top_down():
  adapters = parse_file()
  device_joltage = adapters[-1]
  arr_map = defaultdict(lambda: 0, {device_joltage: 1})
  arr_map = calculate_arrangements(adapters, arr_map, 0)
  print(f'The given adapters can be arranged in {arr_map[0]} ways.')
  

def calculate_adapters_arr_bottom_up():
  adapters = parse_file()
  device_joltage = adapters[-1]
  arr_map = defaultdict(lambda: 0, {0: 1})
  for a in adapters:
    arr_map[a] += arr_map[a - 1] + arr_map[a - 2] + arr_map[a - 3]
  print(f'The given adapters can be arranged in {arr_map[device_joltage]} ways.')
  
  
calculate_adapters_arr_bottom_up()
