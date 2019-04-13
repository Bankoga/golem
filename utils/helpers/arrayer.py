def get_sizes(shape):
  x_sz = shape
  y_sz = shape
  if type(shape) is tuple:
    x_sz = shape[0]
    y_sz = shape[1]
  return (x_sz,y_sz)

def extract_quadrant(input_ind, resource_data,shape):
  x = input_ind[0]
  x_sz, y_sz = get_sizes(shape)
  if len(input_ind) > 1:
    y = input_ind[1]
    quadrant = resource_data[x:x+x_sz][y:y+y_sz]
  else:
    quadrant = resource_data[x:x+x_sz]
  return quadrant

def get_quantity(resource_data, i, j=None):
  if len(resource_data) > 1:
    try:
      quantity = resource_data[i][j]
    except:
      quantity = 0
  else:
    try:
      quantity = resource_data[i]
    except:
      quantity = 0
  return quantity
