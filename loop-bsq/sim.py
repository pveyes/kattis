import sys

n = int(sys.stdin.readline())

class KNode:
  def __init__(self, ch):
    self.ch = ch
    self.next = None
    self.prev = None

for i in range(n):
  ln = sys.stdin.readline().strip()

  h = KNode("")
  p = h
  t = h

  for ch in ln:
    if ch == "<":
      if p.prev is not None:
        pn = p.next
        p = p.prev
        p.next = pn

      if p.next is None:
        t = p
    elif ch == "]":
      p = t
    elif ch == "[":
      p = h
    else:
      n = KNode(ch)
      n.prev = p

      if p.next is None:
        p.next = n
        t = n
      else:
        pn = p.next
        pn.prev = n
        n.next = pn
        p.next = n

      p = p.next

  while h is not None:
    print(h.ch, end="")
    h = h.next
  print()