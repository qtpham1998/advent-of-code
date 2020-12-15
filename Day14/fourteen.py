import re


def load_input():
  with open('fourteen_input.txt', 'r') as file:
    return map(lambda l: l.strip(), file.readlines())
  
  
def to_bit_string(num, length):
  return f'{num:b}'.zfill(length)


def apply_bitmask(num, mask):
  bit_string = to_bit_string(num, len(mask))
  zeroed_mask = int(mask.replace('X', '0'), 2)
  ones_mask = int(mask.replace('X', '1'), 2)
  return (int(''.join(bit_string), 2) | zeroed_mask) & ones_mask


def parse_mem_instr(instr):
  pattern = '^mem\\[(\\d+)\\] = (\\d+)$'
  matches = re.match(pattern, instr)
  addr = int(matches.group(1))
  value = int(matches.group(2))
  return addr, value


def run_program():
  instructions = load_input()
  memory = {}
  mask = ''
  for instr in instructions:
    if instr.startswith('mask'):
      mask = instr[7:]
    else:
      addr, value = parse_mem_instr(instr)
      value = apply_bitmask(value, mask)
      memory[addr] = value
  print(f'The sum of all values in memory is {sum(memory.values())}')
  
  
def get_possible_addresses(addr):
  addresses = [addr]
  x_indexes = [i for i, ltr in enumerate(addr) if ltr == 'X']
  for x in x_indexes:
    new_addrs = []
    for ad in addresses:
      ad[x] = '0'
      new_addrs.append(ad.copy())
      ad[x] = '1'
      new_addrs.append(ad)
    addresses = new_addrs
  return list(map(lambda a: int(''.join(a), 2), addresses))


def decode_mem_address(addr, mask):
  bit_string = list(to_bit_string(addr, len(mask)))
  for i, m in enumerate(mask):
    if m != '0':
      bit_string[i] = m
  return get_possible_addresses(bit_string)


def run_program_v2():
  instructions = load_input()
  memory = {}
  mask = ''
  for instr in instructions:
    if instr.startswith('mask'):
      mask = instr[7:]
    else:
      addr, value = parse_mem_instr(instr)
      addresses = decode_mem_address(addr, mask)
      for addr in addresses:
        memory[addr] = value
  print(f'The sum of all values in memory is {sum(memory.values())}')
  

run_program_v2()