from secrets import SystemRandom

pg_rng = SystemRandom()

def draw(set_size):
  return pg_rng.randint(0,set_size-1)

def draw_from(drawable):
    ind = draw(len(drawable))
    return drawable[ind]

def roll(n_sides):
  return pg_rng.randint(1,n_sides)