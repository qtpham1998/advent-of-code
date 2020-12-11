def find_two_entries_sum(entries, total):
  for i, num1 in enumerate(entries):
    for j in range(i + 1, len(entries)):
      num2 = entries[j]
      for k in range(j + 1, len(entries)):
        num3 = entries[k]
        if num1 + num2 + num3 == total:
          return num1, num2, num3
  return 0, 0, 0
  
  
def find_multiple(total):
  entries = []
  with open('one_input.txt', 'r') as file:
    line = file.readline().strip()
    while line:
      entries.append(int(line))
      line = file.readline().strip()
  
  num1, num2, num3 = find_two_entries_sum(entries, total)
  print(f"The entries summing to {total} are {num1}, {num2} and {num3}. Their "
        f"product is {num1 * num2 * num3}")

find_multiple(2020)