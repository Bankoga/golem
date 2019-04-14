def build_lineage_id(itr):
  res = ''
  for i in itr:
    if i is None:
      break
    elif res == '':
      res = i
    else:
      res = f'{res}-{i}'
  return res