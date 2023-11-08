import sys

ch = sys.stdin.readline().rstrip()
sen = sys.stdin.readline().rstrip().split()

dc = dict()
ss = set()
wr = False

if len(ch) != len(sen):
  print("False")
  exit()

for i in range(len(sen)):
  hc = dc.get(ch[i])

  if hc == None:
    if sen[i] in ss:
      print("False")
      exit()
    else:
      ss.add(sen[i])
      hc = sen[i]
      dc[ch[i]] = sen[i]
  
  if hc != sen[i]:
    print("False")
    exit()

print("True")