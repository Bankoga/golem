"""
A file for utils that don't currently have a place to live.
This should be refactored on a regular basis during active development to keep method count low.
"""

from heapq import merge, heappush, heappop

def input_sort(inputs):
  pass

def merge_sort(m):
  if len(m) <= 1:
      return m

  middle = len(m) // 2
  left = m[:middle]
  right = m[middle:]

  left = merge_sort(left)
  right = merge_sort(right)
  return list(merge(left, right))

def heapsort(iterable):
  h = []
  for value in iterable:
    heappush(h, value)
  return [heappop(h) for i in range(len(h))]