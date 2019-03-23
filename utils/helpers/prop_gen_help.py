from secrets import SystemRandom

from components.axioms.props import pg_data

pg_rng = SystemRandom()

def draw(set_size):
  return pg_rng.randint(0,set_size-1)

def draw_from(drawable):
    ind = draw(len(drawable))
    return drawable[ind]

def roll(n_sides):
  return pg_rng.randint(1,n_sides)

def produce_syllables(num_syllables):
  res = []
  max_len = len(pg_data['syllables'])
  for i in range(num_syllables):
    ind = draw(max_len)
    if ind == max_len:
      sylb = draw_from(pg_data['vowels'])
    else:
      sylb = draw_from(pg_data['syllables'])
    res.append(sylb)
  return res

def roll_for_syllables():
  res_roll = roll(100)
  if 1 <= res_roll and res_roll <= 10:
    num_syllables = 1
  elif 11 <= res_roll and res_roll <= 70:
    num_syllables = 2
  elif 71 <= res_roll and res_roll <= 80:
    num_syllables = 3
  elif 81 <= res_roll and res_roll <= 90:
    num_syllables = 4
  else:
    num_syllables = 5
  return produce_syllables(num_syllables)

def roll_name():
  sylbs = roll_for_syllables()
  res = ''
  for sylb in sylbs:
    join_roll = roll(4)
    if join_roll == 1:
      res = f'{res}{sylb}'
    elif join_roll == 2:
      res = f'{res}_{sylb}'
    elif join_roll == 2:
      res = f'{res}__{sylb}'
    else:
      res = f'{res}___{sylb}'
  return res

# def rel_label_gen(parent, example_child, prefix=None,suffix=None):
#   obj_type_name = type(example_child).__name__
# Syllables can be placed together to form one word, or separated by spaces or hyphens.
#   return []