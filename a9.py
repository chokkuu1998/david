ss=input()
l=[]
for i in range(0,len(ss)):
    for j in range(i+2,len(ss)+1):
        a=ss[i:j]
        if a==a[::-1]:
            l.append(a)
l.sort()
for i in range(0,len(l)):
    print(l[i])
