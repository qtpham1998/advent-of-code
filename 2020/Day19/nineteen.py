import re


def parse_rule(rule):
  pattern = '(\\d+): ("(\\w)"|[\\d |]+)'
  matches = re.match(pattern, rule)
  key = int(matches.group(1))
  if matches.group(3):
    return key, matches.group(3)
  else:
    subrules = []
    for alt in matches.group(2).split(' | '):
      subrules.append(list(map(lambda r: int(r), alt.split(' '))))
    return key, subrules


def parse_rules(rules_list):
  rules_dict = {}
  for r in rules_list:
    key, rules = parse_rule(r)
    rules_dict[key] = rules
  return rules_dict


def load_input():
  with open('nineteen_input.txt', 'r') as file:
    content = file.read().split('\n\n')
    rules = parse_rules(content[0].split('\n'))
    messages = content[1].strip().split('\n')
    return rules, messages


def match_rule_aux(rules_dict, rule, msg):
  if not msg:
    return False, []
  if isinstance(rules_dict[rule], str):
    return rules_dict[rule] == msg[0], [msg[1:]]
  else:
    candidates = []
    for alt in rules_dict[rule]:
      rule_match = True
      remain = [msg]
      for rem in remain:
        for r in alt:
          sub_match, remain = match_rule_aux(rules_dict, r, rem)
          if not sub_match:
            rule_match = False
            break
        if rule_match:
          candidates += remain
    return len(candidates) > 0, candidates


def match_rule(rules_dict, rule, msg):
  match, remain = match_rule_aux(rules_dict, rule, msg)
  return match and not remain


def match_rule_zero():
  rules_dict, messages = load_input()
  count = 0
  for msg in messages:
    match = match_rule(rules_dict, 0, msg)
    if match:
      count += 1
      # print(f'The message {msg} matches the rule 0')
  print(f'The number of messages matching rule 0 is {count}')
  

match_rule_zero()
