from math import floor, ceil

ROWS = 127
COLUMNS = 7


def find_row(seq):
  lower = 0
  upper = ROWS
  for s in seq:
    if s == 'F':
      upper = floor((upper + lower) / 2)
    else:
      lower = ceil((upper + lower) / 2)
  return lower


def find_column(seq):
  lower = 0
  upper = COLUMNS
  for s in seq:
    if s == 'L':
      upper = floor((upper + lower) / 2)
    else:
      lower = ceil((upper + lower) / 2)
  return lower


def find_seat(seq):
  r = find_row(seq[:7])
  c = find_column(seq[7:])
  seat_id = r * 8 + c
  print(f"The seat is at row {r}, column {c}, with ID {seat_id}")
  return seat_id
  

def find_max_seat():
  with open('five_input.txt', 'r') as file:
    max_seat = 0
    line = file.readline().strip()
    while line:
      max_seat = max(max_seat, find_seat(line))
      line = file.readline().strip()
    print(f"The maximum seat is {max_seat}")


def find_missing_seat():
  with open('five_input.txt', 'r') as file:
    max_seat = 0
    min_seat = 100
    total_ids = 0
    line = file.readline().strip()
    while line:
      seat_id = find_seat(line)
      min_seat = min(min_seat, seat_id)
      max_seat = max(max_seat, seat_id)
      total_ids += seat_id
      line = file.readline().strip()
    min_seat -= 1
    total_sum = max_seat * (max_seat + 1) / 2
    min_sum = min_seat * (min_seat + 1) / 2
    print(f"The missing seat ID is {total_sum - total_ids - min_sum}")
    

find_missing_seat()