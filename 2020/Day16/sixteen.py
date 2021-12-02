import re


def parse_rules(input):
  rules = {}
  for rule in input.split('\n'):
    pattern = '^([\\w ]+): (\\d+)-(\\d+) or (\\d+)-(\\d+)$'
    matches = re.match(pattern, rule)
    field = matches.group(1)
    range_tuples = [(int(matches.group(2)), int(matches.group(3))),
                    (int(matches.group(4)), int(matches.group(5)))]
    rules[field] = range_tuples
  return rules


def get_ticket(ticket):
  return list(map(lambda n: int(n), ticket.split('\n')[1].split(',')))


def parse_nearby_tickets(tickets):
  return [list(map(lambda n: int(n), t.split(',')))
          for t in tickets.split('\n')[1:]]
  

def load_input():
  with open('sixteen_input.txt', 'r') as file:
    sections = file.read().split('\n\n')
    rules = parse_rules(sections[0])
    ticket = get_ticket(sections[1])
    nearby_tickets = parse_nearby_tickets(sections[2].strip())
    return rules, ticket, nearby_tickets
    

def check_field_range_validity(ranges, value):
  """ Whether the value satisfies one of given ranges """
  return any([lwr <= value <= upr for lwr, upr in ranges])


def get_rules_validity(rules, value):
  """ Which rules the value satisfies in form of a dict{rule: bool} """
  return {rule: check_field_range_validity(ranges, value)
          for rule, ranges in rules.items()}


def check_ticket_validity(rules, ticket):
  """ Whether ticket is valid and the value that doesn't satisfy any rule,
  if there exist one """
  fields_validity = [any(get_rules_validity(rules, value).values())
            for value in ticket]
  try:
    return False, ticket[fields_validity.index(False)]
  except ValueError:
    return True, 0


def calc_error():
  rules, _, nearby_tickets = load_input()
  error_rate = 0
  for ticket in nearby_tickets:
    error_rate += check_ticket_validity(rules, ticket)[1]
  print(f'The ticket scanning error rate is {error_rate}')


def filter_fields(rules, nearby_tickets):
  """ Get possible fields for each position.
      Returns a list of candidates, indexed by position on the ticket """
  f_candidates = [set(rules.keys()) for _ in range(len(rules))]
  nearby_tickets = \
    filter(lambda t: check_ticket_validity(rules, t)[0], nearby_tickets)
  for ticket in nearby_tickets:
    for i, v in enumerate(ticket):
      rules_validity = get_rules_validity(rules, v)
      candidates = [p[0] for p in filter(lambda p: p[1],
                                              rules_validity.items())]
      f_candidates[i] = f_candidates[i].intersection(set(candidates))
  return f_candidates


def identify_fields(rules, nearby_tickets):
  fields = filter_fields(rules, nearby_tickets)
  set_fields = set()
  n_rules = len(fields)
  while len(set_fields) < n_rules:
    for i, f_set in enumerate(fields):
      if len(f_set) == 1:
        set_fields = set_fields.union(f_set)
      else:
        fields[i] = f_set.difference(set_fields)
  return {pos: next(iter(rule)) for pos, rule in enumerate(fields)}


def multiply_destination_values():
  rules, ticket, nearby_tickets = load_input()
  fields = identify_fields(rules, nearby_tickets)
  product = 1
  for pos, rule in fields.items():
    if rule.startswith('departure'):
      product *= ticket[pos]
  print(f'The departure values multiplied together give {product}')
  

multiply_destination_values()