import sys

n = int(sys.stdin.readline())

ans = 0

for i in range(n):
  a = sys.stdin.readline().rstrip()
  if a == "O":
    ans |= (1 << (n-i-1))

at = 0
for i in range(n):
  if ans & (1 << i):
    at += 1 << i
print(at)

