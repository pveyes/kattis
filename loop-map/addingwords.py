import sys

wi = dict()
iw = dict()

def calc(expr):
  sm = 0
  sign = 1

  for i in range(len(expr)):
    if i % 2 == 0:
      ii = wi.get(expr[i])
      if ii is None:
        return 'unknown'
      else:
        sm += ii * sign
    else:
      sign = -1 if expr[i] == '-' else 1

  return iw.get(sm, 'unknown')

while True:
  line = sys.stdin.readline().rstrip()
  if line == '':
    break

  lp = line.split()
  cmd = lp[0]

  if cmd == 'def':
    w, i = lp[1:]
    ii = int(i)

    pw = iw.get(ii)
    if pw is not None and wi.get(pw) is not None:
      del wi[pw]
      del iw[ii]

    if wi.get(w) is not None:
      del iw[wi[w]]

    wi[w] = ii
    iw[ii] = w
  elif cmd == 'clear':
    iw.clear()
    wi.clear()
  elif cmd == 'calc':
    w = calc(lp[1:])
    print(" ".join(lp[1:]), w)
  
