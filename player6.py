k,l=map(str,input().split())
for i in range(len(k)):
    if(k.count(k[i])==l.count(l[i])):
        print("yes")
        break
    else:
        print("no")
        break
