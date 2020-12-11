import re


def validate_passport_field(key, value):
  if key == 'byr':
    try:
      int_value = int(value)
    except ValueError:
      return False
    return 1920 <= int_value <= 2002
  elif key == 'iyr':
    try:
      int_value = int(value)
    except ValueError:
      return False
    return 2010 <= int_value <= 2020
  elif key == 'eyr':
    try:
      int_value = int(value)
    except ValueError:
      return False
    return 2020 <= int_value <= 2030
  elif key == 'hgt':
    try:
      int_value = int(value[:-2])
    except ValueError:
      return False
    if value.endswith('cm'):
      return 150 <= int_value <= 193
    elif value.endswith('in'):
      return 59 <= int_value <= 76
  elif key == 'hcl':
    return value[0] == '#' and len(value) == 7 and \
           bool(re.compile(r'[a-f0-9]*').search(value[1:]))
  elif key == 'ecl':
    return value in ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']
  elif key == 'pid':
    return len(value) == 9 and value.isnumeric()
  else:
    return True
  

def passport_processing():
  required_fields = {'byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid'}
  with open('four_input.txt', 'r') as file:
    line = file.readline().strip()
    valid_passports = 0
    curr_fields = set()
    while line:
      fields = line.split(' ')
      for f in fields:
        pair = f.split(':')
        if validate_passport_field(pair[0], pair[1]):
          curr_fields.add(pair[0])
        else:
          print(f"Invalid field is {pair[0]} with value {pair[1]}\n")
      
      line = file.readline().strip()
      if not line:
        if required_fields.issubset(curr_fields):
          valid_passports += 1
        curr_fields = set()
        line = file.readline().strip()
    print(f"The number of valid passports is {valid_passports}")
