ss=0
kk=0
ll=[]
vv=input()
for i in v:
  if i not in ll:
    ll.append(i)
    kk+=1
    if ss<kk:
       ss=kk
  else:
    kk=0
print(ss)    
