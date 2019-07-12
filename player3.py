s=int(input())
r=0
while(s>0):
  digit=s%10
  r=r*10+digit
  s=s//10
print(r)
