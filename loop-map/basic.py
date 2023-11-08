import sys

lbs = []
cms = dict()
v = dict()

for line in sys.stdin:
  lp = line.rstrip().split(" ")
  if (len(lp) == 0 or lp[0] == ""):
    break

  lb = int(lp[0])
  lbs.append(lb)
  cms[lb] = lp[1:]

def int_over(num):
  num = num & 0xFFFFFFFF
  if num & 0x80000000:
    num = num - 0x100000000
  return num

def to_int(k):
  if k.isnumeric() or k[0] == "-":
    return int(k)

  return v.get(k, 0)

def eval_ar(xi, op, yi):
  if op == '+':
    return int_over(xi + yi)
  elif op == '-':
    return int_over(xi - yi)
  elif op == '*':
    return int_over(xi * yi)
  elif op == '/':
    return int_over(int(xi / yi))

def run_let(expr):
  k = expr[0]
  s = expr[2:]

  if len(s) == 3:
    x, op, y = s
    r = eval_ar(to_int(x), op, to_int(y))
  else:
    r = to_int(s[0])

  v[k] = r

def run_print(expr, end):
  if expr[0][0] == "\"":
    st = " ".join(expr).replace("\"", "")
    print(st, end=end)
  else:
    sv = to_int(expr[0])
    print(sv, end=end)

def eval_cond(expr):
  x, op, y = expr

  xi = to_int(x)
  yi = to_int(y)

  if op == "=":
    return xi == yi
  elif op == ">":
    return xi > yi
  elif op == "<":
    return xi < yi
  elif op == "<>":
    return xi != yi
  elif op == "<=":
    return xi <= yi
  elif op == ">=":
    return xi >= yi

slbs = sorted(lbs)

def run(cp):
  lb = slbs[cp]
  cm = cms[lb]
  cmd = cm[0]
  expr = cm[1:]

  if cmd == 'LET':
    run_let(expr)
  elif cmd == "PRINT":
    run_print(expr, "")
  elif cmd == "PRINTLN":
    run_print(expr, "\n")
  elif cmd == "IF":
    b = eval_cond(expr[0:3])
    if b:
      nlb = int(expr[5])
      cp = slbs.index(nlb)
      return run(cp)

  return cp + 1

p = 0
while p < len(slbs):
  p = run(p)
