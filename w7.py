a=input()
temp=""
for j in range(len(a)):
    for i in range(i,len(a)):
        k=a[j:i+1]
        if k==k[::-1] and len(k)>len(temp):
           temp=k
print(temp)
