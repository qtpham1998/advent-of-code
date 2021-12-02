def validate_pwd(min_n, max_n, c, pwd):
  return min_n <= pwd.count(c) <= max_n


def validate_pwd_pos(pos1, pos2, c, pwd):
  return (pwd[pos1 - 1] == c) ^ (pwd[pos2 - 1] == c)


def count_valid_pwd(validate_func):
  valid_pwds = 0
  with open('two_input.txt', 'r') as file:
    line = file.readline().strip()
    while line:
      splits = line.split(': ')
      pwd = splits[1]
      splits = splits[0].split(' ')
      c = splits[1]
      splits = splits[0].split('-')
      n1, n2 = int(splits[0]), int(splits[1])
      if validate_func(n1, n2, c, pwd):
        valid_pwds += 1
      line = file.readline().strip()

  print(f"The number of valid passwords are {valid_pwds}")


count_valid_pwd(validate_pwd_pos)
