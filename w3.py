c,d=map(str,input().split())
count=0
for i in range(len(c)):
    #for j in range(0,len(d)):
    if(c[i]!=d[i]):
        count=count+1
if(count==1):
    print("yes")
else:
    print("no")
