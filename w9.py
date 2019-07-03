zz=int(input())
nn=list(map(int,input().split()))
x=0
for i in range(zz):
    if sum(nn[:i])==sum(nn[i+1:]):
        x=x+1
if x>0:
    print("yes")
else:
    print("no")
