Consume images in N(3) channels
Each channel is an array of values equal to the number of channels
So we need to put each channel into a type specific matrix


init
- size of eye target filter
from math import *
mat_sz = 64
row_sz = int(math.sqrt(mat_sz))
col_sz = int(math.sqrt(mat_sz))
OR
row_sz, col_sz, num_ch = imdat.shape

- pct cals for edge lengths
diam_d = 22
diam_b = 2.5
diam_c = 5.5
diam_rat_b = diam_b/diam_d
diam_rat_c = diam_c/diam_d

inr_hght = int(diam_rat_c*row_sz)
inr_wdth = int(diam_rat_c*col_sz)

Y = np.arange(mat_sz).reshape(row_sz,col_sz)
Y

print("colxrow: {0}x{1}\nwxh: {2}x{3}".format(col_sz, row_sz, inr_wdth, inr_hght))

run
- determine starting index
if (new_image):
  center target on middle of image
  start_row = int(0 + (row_sz/2) - (inr_hght/2))
  start_col = int(0 + (col_sz/2) - (inr_wdth/2))
else:
  update from last ts decoder output
  start_row = ?
  start_col = ?

- calc ending index
  end_row = start_row+inr_hght
  end_col = start_col+inr_wdth

- pull values from array
Y[np.ix_(range(start_row,end_row),range(start_col,end_col))]

- zero out outside values
- zero out empty cells

sz_statblock = (len_abs,len_b,len_c,len_d) => {
  return `Filter Props:
  parafvea_sz: ${len_b}x${len_b}=${Math.pow(len_b,2)}px
  perifvea-macula_sz: ${len_c}x${len_c}=${Math.pow(len_c,2)}px
  window_sz: ${len_abs}x${len_abs}=${Math.pow(len_abs,2)}px`
}
sz_stat = (len_abs,hq_sz) => {
  half_len = Math.ceil(len_abs/2)
  len_b = Math.ceil(diam_rat_b*half_len)*2
  len_c = Math.ceil(diam_rat_c*half_len)*2
  stats = 'Using len_abs:\n'+sz_statblock(len_abs,len_b,len_c)
  if (typeof hq_sz != 'undefined') {
    half_len = Math.ceil(hq_sz/diam_rat_c)/2
    len_b = Math.ceil(diam_rat_b*half_len)*2
    len_c = Math.ceil(diam_rat_c*half_len)*2
    console.log('Using hq:\n'+sz_statblock(half_len*2,len_b,len_c))
  }
  return stats
}