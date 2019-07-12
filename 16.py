#dispaly prime numbers between two intervals
inp=list(map(int,input().split()))
final=[]
for q in range(inp[0],inp[1]):
    if q== 2:  # check before the given input is 2 or not
        final.append(str(q))
    else:
        temp = 0
        for i in range(2, q):  # check the palindomic rule
            if q% i == 0:
                temp = 1
                break
        if temp != 1:
            if q!=1:
                final.append(str(q))
print(" ".join(final))
