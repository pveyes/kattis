import sys

n = int(sys.stdin.readline())

d = dict()
c = set()

for i in range(n):
  f = ",".join(sorted(sys.stdin.readline().split()))
  d[f] = d.get(f, 0) + 1

m = 0
for k in d:
  m = max(m, d[k])

t = 0
for k in d:
  if d[k] == m:
    t += m

print(t)
