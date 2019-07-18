r,y=map(int,input().split())
t=list(map(int,input().split()[:r]))
for c in range (0,y):
	t=[t[-1]]+t[:-1]
for l in t:
	print(l,end=" ")
