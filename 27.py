g=input()
h=g.lstrip('-').replace('.','',1).isdigit()
if(h==True):
  print("Yes")
else:
  print("No")
