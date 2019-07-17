a = int(input())
b = list(map(int,input().split()[:a]))
c = sorted(b)
for i in c:
    print(i,end=" ")
