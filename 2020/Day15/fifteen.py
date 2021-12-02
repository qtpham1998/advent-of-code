STARTING_NUMS = [6, 19, 0, 5, 7, 13, 1]
LIMIT = 30000000


def memory_game():
  memory = {}
  for i, num in enumerate(STARTING_NUMS[:-1]):
    memory[num] = i + 1
  
  last_num = STARTING_NUMS[-1]
  for last_turn in range(len(STARTING_NUMS), LIMIT):
    if last_num not in memory.keys():
      memory[last_num] = last_turn
      last_num = 0
    else:
      num = last_turn - memory[last_num]
      memory[last_num] = last_turn
      last_num = num
  print(f'The 30000000 number is {last_num}')


memory_game()
