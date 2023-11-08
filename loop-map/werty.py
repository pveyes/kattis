import sys

wr = {
  '1': '`',
  '2': '1',
  '3': '2',
  '4': '3',
  '5': '4',
  '6': '5',
  '7': '6',
  '8': '7',
  '9': '8',
  '0': '9',
  '-': '0',
  '=': '-',
  # 2nd line
  'W': 'Q',
  'E': 'W',
  'R': 'E',
  'T': 'R',
  'Y': 'T',
  'U': 'Y',
  'I': 'U',
  'O': 'I',
  'P': 'O',
  '[': 'P',
  ']': '[',
  '\\': ']',
  # 3rd line
  'S': 'A',
  'D': 'S',
  'F': 'D',
  'G': 'F',
  'H': 'G',
  'J': 'H',
  'K': 'J',
  'L': 'K',
  ';': 'L',
  '\'': ';',
  # 4th line
  'X': 'Z',
  'C': 'X',
  'V': 'C',
  'B': 'V',
  'N': 'B',
  'M': 'N',
  ',': 'M',
  '.': ',',
  '/': '.'
}

def get_char(w: str):
  return wr[w]
  
def get_word(w: str):
  return ''.join(map(get_char, w))

lc = 0
while True:
  l = sys.stdin.readline().rstrip()
  r = map(get_word, l.split())
  print (' '.join(r))
  lc += len(l)
  if lc >= 10000 or l == '':
    break