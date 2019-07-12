nn,qq=map(int,input().split())
ll=list(map(int,input().split()))
ss=0
tt=[]
for i in range(qq):
    aa,bb=map(int,input().split())
    t=list(l[aa-1:bb])
    for j in t:
        ss=ss+j 
    print(ss)
    ss=0
