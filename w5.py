x=int(input())
l=list(map(int,input().split()))
l1=sorted(2)
if(len(l2)%2==0):
    while(len(l1)!=0):
        print(max(l2),end=" ")
        print(min(l2),end=" ")
        l2.remove(max(l2))
        l2.remove(min(l2))
else:
    while(len(l2)!=0):
        if(len(l2)!=1):
            print(max(l2),end=" ")
            print(min(l2),end=" ")
            l2.remove(max(l2))
            l2.remove(min(l2))
        else:
            print(*l2,end=" ")
            break
