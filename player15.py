g=input()
d=0;
for l in g:
  if(g.count(l)>d):
    d=g.count(l)
    g=l
print (g)   
