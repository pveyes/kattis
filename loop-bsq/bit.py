import sys

def set_bit(v, idx):
  return (v | (1 << idx))

def clr_bit(v, idx):
  return (v & (~(1 << idx)))

def get_bit(v, idx):
  return (v & (1 << idx))

while True:
  line = sys.stdin.readline().rstrip()  
  if line == "0":
    break

  v = 0
  bset = 0
  n = int(line)
  for i in range(n):
    intr = sys.stdin.readline().rstrip().split()
    cmd = intr[0]
    ai = int(intr[1])

    if cmd == "SET":
      v = set_bit(v, ai)
    elif cmd == "CLEAR":
      v = clr_bit(v, ai)
    elif cmd == "AND":
      bi = int(intr[2])

      is_rseta = get_bit(bset, ai)
      is_rsetb = get_bit(bset, bi)

      a = get_bit(v, ai)
      b = get_bit(v, bi)

      if (not a and is_rseta) or (not b and is_rsetb):
        v = clr_bit(v, ai)
        bset = set_bit(bset, ai)
      elif is_rseta and is_rsetb:
        r = a and b
        v = set_bit(v, ai) if r else clr_bit(v, ai)
      else:
        bset = clr_bit(bset, ai)
        continue
    elif cmd == "OR":
      bi = int(intr[2])

      is_rseta = get_bit(bset, ai)
      is_rsetb = get_bit(bset, bi)

      a = get_bit(v, ai)
      b = get_bit(v, bi)

      if a or b:
        v = set_bit(v, ai)
        bset = set_bit(bset, ai)
      elif is_rseta and is_rsetb:
        r = a or b
        v = set_bit(v, ai) if r else clr_bit(v, ai)
      else:
        bset = clr_bit(bset, ai)
        continue
    
    bset = set_bit(bset, ai)
    
  for i in range(32):
    idx = 31-i
    bv = get_bit(v, idx)
    is_rset = get_bit(bset, idx)
    bt = 1 if bv else 0
    print(bt if is_rset else "?", end="")
  print()