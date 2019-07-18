g=input()
d=0;
for i in g:
  if(g.count(i)>d):
    d=g.count(i)
    g=i
print (g)   
