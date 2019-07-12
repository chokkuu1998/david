nin,m=map(int,input().split())
ee=[]
for i in range(m):
  ee.append(list(map(int,input().split())))
cost=10000000
fin=0
for i in range(m):
  if ee[i][0]==1:
    s=ee[i][1]
    c=ee[i][2]
    for j in range(i+1,m):
      if ee[j][0]==s:
        s=ee[j][1]
        c+=ee[j][2]
    if c<cost and s==nin:
      cost=c
      fin+=1
if fin==0:
  print(-1)
else:
  print(cost)
