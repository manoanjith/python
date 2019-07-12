def fact(g):
  if g==0:
    return 1
  else:
    return g*fact(g-1)
g=int(input())
print(fact(g))
