ss,aa=map(str,input().split())
l=[]
if aa in sa:
    print(aa)
else:
    for i in range(0,len(aa)):
        for j in range(0,len(aa)):
            if ss[i]==aa[j]:
                l.append(s[i])
print(''.join(l),end="")
