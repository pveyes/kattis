import sys 

while True:
    n, m = map(int, sys.stdin.readline().split())
    if n == 0 and m == 0:
        break

    nSet = set()
    mSet = set()

    ni = 0

    for i in range(n):
        nSet.add(int(sys.stdin.readline()))
    for i in range(m):
        mSet.add(int(sys.stdin.readline()))

    print(len(nSet & mSet))