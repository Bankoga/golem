from utils.helpers.chaos import draw, draw_from, roll

from components.axioms.props import name_gen_data

def get_sound_type_of_char(character):
  return 'unrecognized'

def produce_consonant():
  return draw_from(name_gen_data['consonants'])

def produce_vowel():
  return draw_from(name_gen_data['vowels'])

def produce_arb_syllable():
  sylb = 'No'
  res_roll = roll(3)
  if 1 == res_roll:
    sylb = f'{produce_consonant()}{produce_vowel()}'
  elif 2 == res_roll:
    sylb = f'{produce_consonant()}{produce_consonant()}{produce_vowel()}'
  elif 3 == res_roll:
    sylb = f'{produce_consonant()}{produce_vowel()}{produce_vowel()}'
  return sylb

def produce_syllables(num_syllables):
  res = []
  max_len = len(name_gen_data['syllables'])
  for i in range(num_syllables): # pylint: disable=unused-variable
    ind = draw(max_len)
    if ind == max_len:
      sylb = draw_from(name_gen_data['vowels'])
    else:
      sylb = draw_from(name_gen_data['syllables'])
    res.append(sylb)
  return res

def roll_for_syllables():
  # TODO: convert to use distribution gen rule instead of if-elif-else
  res_roll = roll(100)
  if 1 == res_roll:
    num_syllables = 1
  elif 2 <= res_roll and res_roll <= 24:
    num_syllables = 2
  elif 25 <= res_roll and res_roll <= 50:
    num_syllables = 3
  elif 51 <= res_roll and res_roll <= 60:
    num_syllables = 4
  elif 61 <= res_roll and res_roll <= 70:
    num_syllables = 5
  elif 71 <= res_roll and res_roll <= 80:
    num_syllables = 6
  elif 81 <= res_roll and res_roll <= 90:
    num_syllables = 7
  elif 91 <= res_roll and res_roll <= 99:
    num_syllables = 8
  else:
    num_syllables = 9
  return produce_syllables(num_syllables)

def roll_name():
  sylbs = roll_for_syllables()
  res = ''
  for sylb in sylbs:
      if res == '':
        res = sylb
      else:
        join_roll = roll(2)
        if join_roll == 1:
            res = f'{res}{sylb.lower()}'
        elif join_roll == 2:
          res = f'{res}_{sylb}'
  return res

def kin_label_gen_unique(parent, num_children, prefix=None,suffix=None):
  names = []
  for i in range(num_children): # pylint: disable=unused-variable
    name = f'{parent}_{roll_new_name(names)}'
    names.append(name)
  return names

def roll_new_name(old_names):
  found_name = False
  while not found_name:
    name = roll_name()
    if not name in old_names:
      return name