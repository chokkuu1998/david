chaa,choo=map(int,input().split())
saaa=[]
for p in range(chaa+1,choo+1):
  if p>1:
    for f in range(2,p):
      if(p%f==0):
        break
    else:
      saa.append(f)
print(len(saa)+1)
