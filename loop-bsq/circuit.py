import sys

n = int(sys.stdin.readline())
va = sys.stdin.readline().split()
expr = sys.stdin.readline().split()

pv1 = None
pv2 = None

def is_operator(c):
  return c in ['+', '-', '*']

def get_v(a):
  if a == 1 or a == 0:
    return a
  else:
    idx = ord(a) - ord('A')
    return va[idx] == "T"

i = 0
while len(expr) > 1:
  ex = expr[i]
  while not is_operator(ex):
    i += 1
    ex = expr[i]

  if ex == "-":
    a = expr.pop(i-1)
    expr.pop(i-1)
    i -= 1
    expr.insert(i, 1 if not get_v(a) else 0)
  elif ex == "+":
    a = expr.pop(i-2)
    b = expr.pop(i-2)
    expr.pop(i-2)
    i -= 2
    res = get_v(a) or get_v(b)
    expr.insert(i, 1 if res else 0)
  elif ex == "*":
    a = expr.pop(i-2)
    b = expr.pop(i-2)
    expr.pop(i-2)
    i -= 2
    res = get_v(a) and get_v(b)
    expr.insert(i, 1 if res else 0)

print("T" if expr[0] else "F")