import sys

n = int(sys.stdin.readline())
p = 0
x = 2
ws = set()

for i in range(n):
  word = sys.stdin.readline().rstrip()
  if word in ws and x == 2:
    x = i % 2

  ws.add(word)  
  first = word[0]
  if i > 0 and first != last and x == 2:
    x = i % 2
  last = word[-1]

if x == 2:
  print("Fair game")
else:
  print("Player " + str(x + 1) + " lost")