N=int(input())
count=0
ar=list(map(int,input().split()))[:N]
for i in range (0,N-2):
    for j in range (1,N-1):
        for k in range (2,N):
            if((ar[i]<ar[j]) and (ar[j]<ar[k])):
                count+=1
print(count)
