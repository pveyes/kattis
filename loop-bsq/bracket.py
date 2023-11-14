import sys
from collections import deque

n = int(sys.stdin.readline())

expr = sys.stdin.readline().split()

mx = (10**9 + 7)

def run_op(x, y, op):
  return (x + y if op % 2 == 0 else x * y) % mx

st = deque()
ct = deque([0])
op = 0
for i in range(len(expr)):
  if expr[i] == "(":
    op += 1
    ct.append(0)
  elif expr[i] == ")":
    p = None
    while ct[-1] > 0:
      if p is None:
        p = st.pop()
      else:
        p = run_op(st.pop(), p, op)
      ct[-1] -= 1
    st.append(p)
    op -= 1
    ct.pop()
    ct[-1] += 1
  else:
    st.append(int(expr[i]))
    ct[-1] += 1

print(sum(st) % mx)