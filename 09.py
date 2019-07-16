nn=int(input())
tt=3
ss=3
ll=[]
ll.append(3)
for i in range(1,nn+1):
    if tt==1:
        tt=2*ss
        ss=tt
        ll.append(tt)
    else:
        tt=tt-1
        ll.append(tt)
print(ll[nn-1])
        
