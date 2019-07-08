mm,nn=map(int,input().split())
kk=[]
ss=[]
aa=[int(mm) for mm in input().split() ]
for i in range(0,nn):
    uu,vv=map(int,input().split())
    for j in range(uu-1 ,vv):
        ss.append(aa[j])
    xx=sorted(ss)
    kk.append(min(ss))
    del ss[:]
for zz in range(0,len(kk)):
    print(k[z])
