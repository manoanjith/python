g,h=input().split()
g=int(g)
h=int(h)
P=[]
for c in range(g+1,h):
  sum=0
  temp=c
  while(temp!=0):
    h=temp%10
    sum+=h**3
    temp//=10
  if(c==sum):
    P.append(c)
print(*P)
