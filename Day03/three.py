def count_trees(right, down):
  count = 0
  with open('three_input.txt', 'r') as file:
    x = 0
    line = file.readline().strip()
    while line:
      for _ in range(down):
        line = file.readline().strip()
      if len(line) == 0: break
      x += right
      if line[x % len(line)] == '#': count += 1
  print(f'The number of trees encountered is {count}')
  return count
  
product = 1
for r, d in [(1, 1), (3, 1), (5, 1), (7, 1), (1, 2)]:
  product *= count_trees(r, d)
print(f'Product of trees encountered is {product}')
