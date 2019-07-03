aa,bb = input().split()
c,s = 0,''
for i in range(0,len(aa)):
  k = i
  for j in range(0,len(bb)):
    if aa[k] == bb[j]:
      s += aa[k]
      k += 1
    else:
      break
  if len(s) > c:
    c = len(s)
    p = s
  s = ''
print(p)
