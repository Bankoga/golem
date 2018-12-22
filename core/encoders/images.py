# added a file for the eventual images problem domain code

# HxW = 128x128 window slider with perifovea, and parafovea differentiation. Gets reduced to 32x32 combined map, and 32x32 center only hq map

# Eye Encoder area distribution calcs
var diam_d = 22
var diam_b = 2.5
var diam_c = 5.5
var diam_blind = 3
var d = (Math.PI*Math.pow(diam_d/2,2))
var B = (Math.PI*Math.pow(diam_b/2,2))
var C = (Math.PI*Math.pow(diam_c/2,2)-B)
var blind = Math.PI*Math.pow(diam_blind/2,2)
var D = d - (B+blind+C)
var sum = D + B + C
var pctD = D / sum
var pctB = B / sum
var cnt = 130e6
var cones = 6e6
var rods = 120e6
var dist = function(pct,n,a){return (pct*n)/a}
var totalCnt = (dist(pctD,cnt,D)+dist(pctB,cnt,B));
(dist(pctB,cones,B))*Math.pow(0.001,2);
totalCnt - ((dist(1,rods,D)) + ((dist(0.5,cones,B))*2));
(pctD*cnt/D)/(cones/(B+C));

var len_abs = 128
var half_len = Math.ceil(len_abs/2)
var len_b = Math.ceil(diam_rat_b*half_len)*2
var len_c = Math.ceil(diam_rat_c*half_len)*2

var diam_rat_b = diam_b/diam_d
var diam_rat_c = diam_c/diam_d

var sz_statblock = function(len_abs,len_b,len_c,len_d) {
  return `Filter Props:
  parafvea_sz: ${len_b}x${len_b}=${Math.pow(len_b,2)}px
  perifvea-macula_sz: ${len_c}x${len_c}=${Math.pow(len_c,2)}px
  window_sz: ${len_abs}x${len_abs}=${Math.pow(len_abs,2)}px`
}
var sz_stat = function (len_abs,hq_sz) {
  var half_len = Math.ceil(len_abs/2)
  var len_b = Math.ceil(diam_rat_b*half_len)*2
  var len_c = Math.ceil(diam_rat_c*half_len)*2
  //var len_d = Math.ceil(diam_rat_d*half_len)*2
  var stats = 'Using len_abs:\n'+sz_statblock(len_abs,len_b,len_c)
  if (typeof hq_sz != 'undefined') {
    half_len = Math.ceil(hq_sz/diam_rat_c)/2
    len_b = Math.ceil(diam_rat_b*half_len)*2
    len_c = Math.ceil(diam_rat_c*half_len)*2
  stats+='Using hq:\n'+sz_statblock(half_len*2,len_b,len_c)
  }
  return stats
}