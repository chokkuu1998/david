ss=str(input())
ll=[]
tt=""
rr=0
for i in range(0,len(ss)):
    for j in range(i,len(ss)):
        tt=tt+ss[j]
        if(tt[::-1]==tt):
            rr=len(ss)-len(tt)
            ll.append(rr)
    tt=""
print(min(ll))
