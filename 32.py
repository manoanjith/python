g=input()
h=g.strip()
d=1
for i in range (len(h)):
    if(h[i]==' ' and (h[i]!=h[i+1])):
        d=d+1
if(d>1):
    print(d)
