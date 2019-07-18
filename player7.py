v=input()
l=len(v)
z=[]
for x in range(0,l,2):
    z.append(v[x:x+2][::-1])
print(''.join(z))
