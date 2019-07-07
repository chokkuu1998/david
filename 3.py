nn=int(input())
list=[1000,500,100,50,10,1]
c=0
while n>0:
    for i in range(0,len(list)):
        if n>=list[i]:
            nn=n-list[i]
            c+=1
            break
print(c)
