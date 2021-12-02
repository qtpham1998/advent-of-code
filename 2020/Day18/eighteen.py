from enum import Enum
from collections import deque


class Op(Enum):
  ADD = '+'
  MUL = '*'
  LPR = '('
  RPR = ')'
  
  def precedence(self):
    if self == Op.ADD:
      return 2
    elif self == Op.MUL:
      return 1
    return 0
    
  
def load_input():
  with open('eighteen_input.txt', 'r') as file:
    lines = file.readlines()
    return [tokenize(line) for line in lines]
    

def tokenize(line):
  tokenized_line = []
  for c in line.strip():
    if c.isspace():
      continue
    try:
      tokenized_line.append(int(c))
    except ValueError:
      tokenized_line.append(Op(c))
  return tokenized_line


def eval_op(a, b, op):
  return a + b if op == Op.ADD else a * b


def eval_expr(tokens):
  values = deque()
  ops = deque()
  
  for t in tokens:
    if isinstance(t, int):
      values.append(t)
    elif t == Op.RPR:
      while ops[-1] != Op.LPR:
        values.append(eval_op(values.pop(), values.pop(), ops.pop()))
      ops.pop()
    else:
      if t != Op.LPR:
        while len(ops) > 0 and ops[-1].precedence() >= t.precedence():
          values.append(eval_op(values.pop(), values.pop(), ops.pop()))
      ops.append(t)
      
    # print(f'Values = {values}, Operators = {ops}')
    
  while len(ops) > 0 and len(values) > 1 and ops[-1] != Op.LPR:
      values.append(eval_op(values.pop(), values.pop(), ops.pop()))
  return values.pop()
  

def get_sum_evaluations():
  tokenized_input = load_input()
  total = 0
  for line in tokenized_input:
    total += eval_expr(line)
  print(f'The sum of all expressions is {total}')
  

get_sum_evaluations()
