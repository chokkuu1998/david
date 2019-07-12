AA,BB=map(int,input().split())
CC=list(map(int,input().split()))
pp=list(map(int,input().split()))
qq=[]
rr=0
for i in range(AA):
    x=pp[i]/C[i]
    qq.append(x)
while B>=0 and len(qq)>0:
    mindex=qq.index(max(qq))
    if B>=C[mindex]:
        rr=rr+pp[mindex]
        B=B-C[mindex]
    CC.pop(mindex)
    pp.pop(mindex)
    qq.pop(mindex)
print(rr)
