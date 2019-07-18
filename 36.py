m=input()
s=0
for word in m:
  
  if word=='.'or word=='@'or word=='%'or word=='&'or word=='*'or word=='6'or word=='#'or word=='!'or word=='$' or word=='_':
    s+=1
  
print(s) 
