def parse_file():
  with open('nine_input.txt', 'r') as file:
    numbers = file.read().strip().split('\n')
    return list(map(lambda x: int(x), numbers))


def is_number_valid(precedents, number):
  prec_set = set(precedents)
  for n in prec_set:
    if (number - n) in prec_set:
      return True
  return False


def find_invalid_number():
  numbers = parse_file()
  for i in range(0, len(numbers) - 1):
    j = i + 25
    num = numbers[j]
    if not is_number_valid(numbers[i:j], num):
      return num
  return 0


def find_contiguous_sum(num):
  numbers = parse_file()
  i, j = 0, 2
  total = numbers[0] + numbers[1]
  while total != num:
    if total < num:
      total += numbers[j]
      j += 1
    else:
      total -= numbers[i]
      i += 1
  return numbers[i:j]


contiguous_list = find_contiguous_sum(400480901)
optimum_sum = min(contiguous_list) + max(contiguous_list)
print(f'The contiguous set summing to {400480901} is {contiguous_list}.\n')
print(f'The sum of its min and max is {optimum_sum}.')