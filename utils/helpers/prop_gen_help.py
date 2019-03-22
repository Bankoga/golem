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
  res_roll = roll(20)
  if 1 <= res_roll and res_roll <= 4:
    num_syllables = 1
  elif 5 <= res_roll and res_roll <= 8:
    num_syllables = 2
  elif 9 <= res_roll and res_roll <= 12:
    num_syllables = 3
  elif 13 <= res_roll and res_roll <= 16:
    num_syllables = 4
  else:
    num_syllables = 5
  return produce_syllables(num_syllables)

# def rel_label_gen(parent, example_child, prefix=None,suffix=None):
#   obj_type_name = type(example_child).__name__
#   return []