nn,tt=map(int,input().split())
aa=list(map(int,input().split()))
dd=0
ii=0
while tt>0:
    tt=tt-86400+aa[ii];
    ii=ii+1
    dd=dd+1
print(dd)
