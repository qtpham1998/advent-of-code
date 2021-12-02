from collections import defaultdict

ACT = '#'
INV = '.'
CYCLES = 6


def load_input():
  grid = defaultdict(lambda: defaultdict(lambda: defaultdict
                    (lambda: defaultdict(lambda: INV))))
  with open('seventeen_input.txt', 'r') as file:
    for x, row in enumerate(file.readlines()):
      for y, elem in enumerate(row.strip()):
        grid[0][0][x][y] = elem
  return grid

  
def display_grid(grid):
  for w, n in grid.items():
    for z, m in n.items():
      print(f'\nz={z}, w={w}')
      rows = sorted(m.items(), key=lambda e: e[0])
      for _, row in rows:
        sorted_row = sorted(row.items(), key=lambda e: e[0])
        r = list(map(lambda e: e[1], sorted_row))
        print(''.join(r))
      

def get_updated_status(curr_status, neighbours):
  active_n = ''.join(neighbours).count(ACT)
  return ACT if active_n == 3 or (active_n == 2 and curr_status == ACT) else INV


def get_neighbours(grid, x, y, z, w):
  neighbours = []
  for l in range(w - 1, w + 2):
    for k in range(z - 1, z + 2):
      for i in range(x - 1, x + 2):
        for j in range(y - 1, y + 2):
          neighbours.append(grid[l][k][i][j])
  return neighbours


def run_cycle(grid):
  new_grid = defaultdict(lambda: defaultdict(lambda: defaultdict
                        (lambda: defaultdict(lambda: INV))))
  w_range, z_range, x_range, y_range = get_ranges(grid)
  for w in w_range:
    for z in z_range:
      for x in x_range:
        for y in y_range:
          curr_status = grid[w][z][x][y]
          grid[w][z][x][y] = '!'
          neighbours = get_neighbours(grid, x, y, z, w)
          new_grid[w][z][x][y] = get_updated_status(curr_status, neighbours)
          grid[w][z][x][y] = curr_status
  return new_grid


def get_ranges(grid):
  w_range = grid.keys()
  z_range = grid[0].keys()
  x_range = grid[0][0].keys()
  y_range = grid[0][0][0].keys()
  return range(min(w_range) - 1, max(w_range) + 2), \
         range(min(z_range) - 1, max(z_range) + 2), \
         range(min(x_range) - 1, max(x_range) + 2), \
         range(min(y_range) - 1, max(y_range) + 2)
  

def run_simulation():
  grid = load_input()
  for cycle_num in range(CYCLES):
    grid = run_cycle(grid)
  return grid
  

def get_active_cells():
  grid = run_simulation()
  active_cells = 0
  for w in grid.values():
    for z in w.values():
      for x in z.values():
        for y in x.values():
          active_cells += ''.join(y).count(ACT)
  print(f'The number of active cells is {active_cells}')
  
  
get_active_cells()
