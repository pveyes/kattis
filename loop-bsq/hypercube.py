import sys

n, a, b = sys.stdin.readline().rstrip().split()

def get_i(s):
  ns = len(s) - 1
  mpx = 1 << ns
  x = 0 if s[0] == '0' else mpx
  if len(s) == 1:
    return x
  px = get_i(s[1:])
  y = px if x == 0 else mpx - px - 1
  return x + y

ai = get_i(a)
bi = get_i(b)
d = max(bi - ai - 1, 0)
print(d)
