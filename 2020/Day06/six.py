from collections import Counter

def count_positive_answers():
  count = 0
  with open('six_input.txt', 'r') as file:
    line = file.readline()
    group_answers = ''
    group_n = 0
    while line:
      if line == '\n':
        frequency = Counter(group_answers)
        for _, freq in frequency.items():
          if freq == group_n:
            count += 1
        
        group_answers = ''
        group_n = 0
      else:
        group_answers += line.strip()
        group_n += 1
      line = file.readline()
  print(f'The sum of counts is {count}')
  
count_positive_answers()