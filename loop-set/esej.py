import sys
import math

a, b = map(int, sys.stdin.readline().split())

wa = []

for i in range(math.ceil(b/2)):
  x = i+1

  w = ""
  while x > 0:
    w = chr(((x-1) % 26) + 97) + w
    x = math.floor((x-1) / 26)

  wa.append(w)

  if (len(wa) >= b):
    break

  wa.append(w)

print(" ".join(wa))
