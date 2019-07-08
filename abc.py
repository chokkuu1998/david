nn=int(input())
list=[];c=0
for i in range(nn):
    row=list(map(int,input().split()))
    lis.append(row)
j=nn-1
for i in range(nn):
    c+=list[i][j]
    j-=1
print(c)
