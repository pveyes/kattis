import sys

for line in sys.stdin:
  l = line.rstrip()
  if l == "":
    break
  
  x0 = 0
  x1 = 0
  for ch in l:
    bn = bin(ord(ch))[2:].zfill(7)
    for b in bn: 
      if b == '0':
        x0 += 1
      else:
        x1 += 1
      
  d0 = x0 % 2
  d1 = x1 % 2
  if d0 == 0 and d1 == 0:
    print("free")
  else:
    print("trapped")
