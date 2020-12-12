import numpy as np
from enum import Enum


class Dir(Enum):
  NORTH = 0
  EAST = 1
  SOUTH = 2
  WEST = 3


class Position:
  def __init__(self):
    self.direction = Dir.EAST
    self.v_pos = 0
    self.h_pos = 0
  
  def move_north(self, dist):
    self.v_pos += dist
  
  def move_south(self, dist):
    self.v_pos -= dist
  
  def move_east(self, dist):
    self.h_pos += dist
  
  def move_west(self, dist):
    self.h_pos -= dist
    
  def rotate_left(self, degrees):
    new_dir_val = (self.direction.value + len(Dir) - degrees // 90) % len(Dir)
    self.direction = Dir(new_dir_val)
  
  def rotate_right(self, degrees):
    self.rotate_left(-degrees)
  
  def move_forward(self, dist):
    dir_func_map = {Dir.NORTH: self.move_north,
                    Dir.SOUTH: self.move_south,
                    Dir.EAST: self.move_east,
                    Dir.WEST: self.move_west}
    dir_func_map[self.direction](dist)

  def __str__(self) -> str:
    h_dir = (Dir.EAST if self.h_pos >= 0 else Dir.WEST).name
    v_dir = (Dir.NORTH if self.v_pos >= 0 else Dir.SOUTH).name
    return f'The final position of the ship is {abs(self.h_pos)} ' \
           f'{h_dir}, {abs(self.v_pos)} {v_dir}.\n'


class Waypoint(Position):
  def __init__(self):
    super().__init__()
    self.h_pos = 10
    self.v_pos = 1
  
  def rotate_left(self, degrees):
    radians = degrees / 180 * np.pi
    self.h_pos, self.v_pos = \
      np.round(self.h_pos * np.cos(radians) - self.v_pos * np.sin(radians)), \
      np.round(self.h_pos * np.sin(radians) + self.v_pos * np.cos(radians))


class Ship(Position):
  def __init__(self, waypoint):
    super().__init__()
    self.waypoint = waypoint
  
  def move_north(self, dist):
    self.waypoint.move_north(dist)
  
  def move_south(self, dist):
    self.waypoint.move_south(dist)
  
  def move_east(self, dist):
    self.waypoint.move_east(dist)
  
  def move_west(self, dist):
    self.waypoint.move_west(dist)
  
  def rotate_right(self, degrees):
    self.waypoint.rotate_right(degrees)
  
  def rotate_left(self, degrees):
    self.waypoint.rotate_left(degrees)
  
  def move_forward(self, dist):
    self.h_pos += dist * self.waypoint.h_pos
    self.v_pos += dist * self.waypoint.v_pos


def load_input():
  with open('twelve_input.txt', 'r') as file:
    return file.readlines()


def update_position(position, action, d):
  action_func_map = {'N': position.move_north,
                     'S': position.move_south,
                     'E': position.move_east,
                     'W': position.move_west,
                     'R': position.rotate_right,
                     'L': position.rotate_left,
                     'F': position.move_forward}
  action_func_map[action](d)
  return position


def run_navigation(use_waypoint=False):
  instructions = load_input()
  ship = Ship(Waypoint()) if use_waypoint else Position()
  for i in instructions:
    ship = update_position(ship, i[0], int(i[1:]))
  print(f'The Manhattan distance from starting position is '
        f'{abs(ship.h_pos) + abs(ship.v_pos)}')


run_navigation(True)
