aa,bb=map(str,input().split())
count=0
for i in range(0,len(aa)):
    for j in range(0,len(bb)):
        if bb[j]==aa[i]:
            count+=1
if count==len(bb):
    print("yes")
else:
    print("no")
