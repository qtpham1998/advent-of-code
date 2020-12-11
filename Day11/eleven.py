import numpy as np
import copy

FLR = '.'
OCP = '#'
FRE = 'L'


def load_input():
  with open('eleven_input.txt', 'r') as file:
    rows = file.read().strip().split('\n')
    layout = map(lambda l: np.array(list(l)), rows)
    return np.array(list(layout))


def get_occupied_neighbour_1(layout, row, col):
  rows, cols = layout.shape
  neighbours = \
    layout[np.maximum(0, row - 1):np.minimum(rows, row + 2),
    np.maximum(0, col - 1):np.minimum(cols, col + 2)]
  
  return np.sum(np.char.count(neighbours, OCP))


def get_occupied_neighbour_2(layout, row, col):
  rows, cols = layout.shape
  neighbours = np.array([])
  vecs = [[0, 1], [1, 1], [1, 0], [1, -1], [0, -1], [-1, -1], [-1, 0], [-1, 1]]
  
  for dx, dy in vecs:
    i = row
    j = col
    while layout[i][j] in ['!', FLR]:
      new_i = np.minimum(rows - 1, np.maximum(0, i + dx))
      new_j = np.minimum(cols - 1, np.maximum(0, j + dy))
      if (i == new_i and dx != 0) or (j == new_j and dy != 0):
        break
      else:
        i = new_i
        j = new_j
      
    neighbours = np.append(neighbours, layout[i][j])
    
  return np.sum(np.char.count(neighbours, OCP))


def get_updated_seat_status(layout, row, col):
  curr_status = layout[row][col]
  if curr_status == FLR: return FLR
  
  try:
    layout[row][col] = '!'

    occupied_neighbours = get_occupied_neighbour_2(layout, row, col)
    if curr_status == FRE and occupied_neighbours == 0:
      return OCP
    elif curr_status == OCP and occupied_neighbours >= 5:
      return FRE
    return curr_status
  finally:
    layout[row][col] = curr_status


def update_seating_layout(layout):
  rows, cols = layout.shape
  return np.array(
    [[get_updated_seat_status(layout, i, j) for j in range(cols)]
     for i in range(rows)])


def run_seating_system(layout):
  updated_layout = update_seating_layout(layout)
  while (layout != updated_layout).any():
    layout = updated_layout
    # print('\nThe new layout is:')
    # print('\n'.join(list(map(lambda l: ''.join(l), layout))))
    updated_layout = update_seating_layout(layout)
  return updated_layout


def get_stable_occupied_seats():
  layout = load_input()
  stable_layout = run_seating_system(layout)
  return np.sum(np.char.count(stable_layout, OCP))


print(f'The number of stable occupied seats are {get_stable_occupied_seats()}')
