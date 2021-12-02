ACC = 'acc'
NOP = 'nop'
JMP = 'jmp'


def parse_instructions():
  with open('eight_input.txt', 'r') as file:
    return file.read().split('\n')
  
  
def run_program(instructions):
  executed_instr = set()
  curr_instr = 0
  accumulator = 0
  instr_order = []
  while True:
    if curr_instr in executed_instr or curr_instr >= len(instructions):
      break
    executed_instr.add(curr_instr)
    instr_order.append(curr_instr)
    instruction = instructions[curr_instr].split(' ')
    command, num = instruction[0], int(instruction[1])
    
    if command == JMP:
      curr_instr += num
    else:
      if command == ACC:
        accumulator += num
      curr_instr += 1
  return accumulator, curr_instr, instr_order


def find_corrupt_instr():
  og_instructions = parse_instructions()
  acc, instr, instr_order = run_program(og_instructions)
  instr_order.reverse()
  for i in instr_order:
    if instr >= len(og_instructions):
      return acc, i
    else:
      instructions = og_instructions.copy()
      instruction = instructions[i].split(' ')
      command = instruction[0]
      if command == ACC:
        continue
      elif command == JMP:
        instructions[i] = NOP + ' ' + instruction[1]
      elif command == NOP:
        instructions[i] = JMP + ' ' + instruction[1]
      acc, instr, _ = run_program(instructions)
      

accumulator, changed_instr = find_corrupt_instr()
print(f"Program ended with accumulator = {accumulator}. The changed "
      f"instruction is at line {changed_instr}.")
