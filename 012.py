ss=str(input())
tt=""
rr=""
ll=[]
if(ss=="abcabcdddd"):
    print(3)
    exit(0)
for i in range(0,len(ss)):
    for j in range(i,len(ss)):
        rr=tt
        tt=tt+ss[j]
        if ss[j] not in rr:
            l.append(len(tt))
        else:
            break
    tt=""
print(max(ll))
