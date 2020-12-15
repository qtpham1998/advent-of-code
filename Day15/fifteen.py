def memory_game():
  starting_numbers = [6, 19, 0, 5, 7, 13, 1]
  memory = {}
  for i, num in enumerate(starting_numbers[:-1]):
    memory[num] = i + 1
  
  last_num = starting_numbers[-1]
  curr_turn = len(starting_numbers) + 1
  while curr_turn <= 30000000:
    if last_num not in memory.keys():
      memory[last_num] = curr_turn - 1
      last_num = 0
    else:
      last_turn = curr_turn - 1
      num = last_turn - memory[last_num]
      memory[last_num] = last_turn
      last_num = num
    curr_turn += 1
  print(f'The 30000000 number is {last_num}')


memory_game()
