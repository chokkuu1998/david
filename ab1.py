nn=int(input())
l=[]
c=0
for i in range(nn):
    l1=[int(x) for x in input().split()]
    l.append(l1)
for i in range(nn):
    for j in range(nn):
        if (i+j)==(nn-1):
            c=c+l[i][j]
print(c)
