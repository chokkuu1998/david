xx=int(input())
tt=[]
for i in range(0,Xx):
    l=list(map(int,input().split()))
    for j in l:
        t.append(j)
print(*sorted(t),end="")
