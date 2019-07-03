nnn,kk=list(map(str,input().split()))
l=[]
for i in nn:
    for j in kk:
        if i==j:
            l.append(i)
print("".join(l))
