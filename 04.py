nnnum,kknum = map(int,input().split())
u = list(map(int,input().split()))
v,w = 0,[]
for i in range(0,len(u)):
  t = i
  for a in range(0,len(u)):
    for l in range(0,kknum):
      if l == kknum-1:
        try:
          v += u[a+i]
        except IndexError:
            t = t-1
            v +=u[t]
      else:
        v += u[i]
    w.append(v)
    v = 0
for i in range(0,len(u),kknum):
  v = sum(u[i:i+kknum])
  w.append(v)
print(*sorted(set(w)))
