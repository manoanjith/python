e,y=input().split()
e=int(e)
y=int(y)
o=[]
if(e>1 and y>1):
	for k in range (e,y+1):
		for l in range (2,k):
			if(k%l==0):
				break
		else:
			o.append(k)
print(len(o))
