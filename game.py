from colorama import Back, Style, Fore
import random

def ntb(n):
  if n == 0:
      return '0'
  digits = []
  while n:
      digits.append(int(n % 6))
      n //= 6
  return ''.join(map(str, digits[::-1]))

def check(a, b, w, bl):
  a = ntb(a).zfill(4)
  b = ntb(b).zfill(4)
  aw = 0
  abl = 0
  n_a = [0,0,0,0,0,0]
  n_b = [0,0,0,0,0,0]
  for digit in a:
    n_a[int(digit)] += 1
  for digit in b:
    n_b[int(digit)] += 1
  for i in range(4):
    if a[i] == b[i]:
      abl += 1
  for i in range(6):
    aw += min(n_a[i], n_b[i])
  aw -= abl
  return (w == aw and bl == abl)

def printColor(s):
  for d in s:
    if(d == '0'): print(Back.WHITE+"  ", end="")
    if(d == '1'): print(Back.BLACK+"  ", end="")
    if(d == '2'): print(Back.RED+"  ", end="")
    if(d == '3'): print(Back.GREEN+"  ", end="")
    if(d == '4'): print(Back.BLUE+"  ", end="")
    if(d == '5'): print(Back.YELLOW+"  ", end="")
  print(Style.RESET_ALL)

while 1:
  table = []
  for i in range(0, int('10000',6)):
    table.append(1)

  print(Fore.WHITE + "Input random first row")
  print("0=W 1=BLA 2=R 3=G 4=BLU 5=Y")
  a = input()

  while 1:
    b = int(input("Number of black "))
    w = int(input("Number of white "))
    pAns = []
    for i in range(0, int('10000',6)):
      if table[i]:
        if check(int(a, 6), i, w, b):
          pAns.append(ntb(i).zfill(4))
        else: table[i] = 0
    l = len(pAns)
    if l < 1: print(Fore.RED + "Something is wrong!!!" + Fore.WHITE)
    elif l == 1:
      print("Answer is ", end="")
      printColor(pAns[0])
      print()
      break
    else: 
      a = random.choice(pAns)
      print("Guess this ", end="")
      printColor(a)
      print(" ", l)
  input("Press Enter to continue...")
  print()