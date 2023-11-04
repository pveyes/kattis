def gen_delta():
  for x in range(-2018, 2019):
    for y in range(-2018, 2019):
      if x ** 2 + y ** 2 == 2018 ** 2:
        yield (x, y)

delta = list(gen_delta())

p = []
n = int(input())
for i in range(n):
  x, y = map(int, input().split())
  p.append((x, y))

pc = set()
c = 0

for i in range(n):
  for d in delta:
    pt = p[i][0] + d[0], p[i][1] + d[1]
    if pt in pc:
      c += 1
  pc.add(p[i])

print(c)