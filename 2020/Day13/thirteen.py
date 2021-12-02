from functools import reduce
from operator import mul


def load_input():
  with open('thirteen_input.txt', 'r') as file:
    content = file.readlines()
    port_arrival_time = int(content[0].strip())
    bus_times = content[1].strip().split(',')
    return port_arrival_time, bus_times
  
  
def get_earliest_departure():
  port_arrival, bus_times = load_input()
  bus_times = filter(lambda x: x != 'x', bus_times)
  bus_times = list(map(lambda x: int(x), bus_times))
  
  next_bus_departures = list(map(lambda b: b * (1 + port_arrival // b), bus_times))
  earliest_departure = min(next_bus_departures)
  index = next_bus_departures.index(earliest_departure)
  
  print(f'The earliest bus that can be taken has ID {bus_times[index]} at '
        f'time {earliest_departure}. The time to wait is '
        f'{earliest_departure - port_arrival}.\n')
  print(f'The ID multiplied by the wait time is '
        f'{bus_times[index] * (earliest_departure - port_arrival)}')
  
  
def build_bus_offset_dict(bus_times):
  bus_offset_dict = {}
  for offset, bt in enumerate(bus_times):
    if bt != 'x':
      bus_offset_dict[int(bt)] = offset
  return bus_offset_dict


def inv(a, N):
  # compute multiplicative inverse (mod N) using fermat's little theorem
  return pow(int(a), N - 2, N)


def chinese_remainder_theorem(bus_times, bus_offset_dict):
  M = reduce(mul, bus_times)
  timestamp = 0
  for i, b in enumerate(bus_times):
    m_i = M // b
    timestamp += (-bus_offset_dict[b] % b) * m_i * inv(m_i, b)
  timestamp %= M
  return timestamp


def get_earliest_timestamp():
  _, bus_times = load_input()
  bus_offset_dict = build_bus_offset_dict(bus_times)
  bus_times = list(bus_offset_dict.keys())
  timestamp = chinese_remainder_theorem(bus_times, bus_offset_dict)
  print(f'The timestamp is {timestamp}')
  

get_earliest_timestamp()
