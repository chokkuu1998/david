aaz,bbx=map(str,input().split())
co=0
for i in range(0,len(aaz)):
    for j in range(0,len(bbx)):
        if aaz[i]==bbx[j]:
            co+=1
if co>=2:
    print("yes")
else:
    print("no")
