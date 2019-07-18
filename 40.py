z=int(input())
g=0
h=1
n=1
for i in range(z):
	print(n,end=' ')
	n=g+h
	g=h
	h=n
