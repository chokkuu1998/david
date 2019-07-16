nn1=int(input())
lli=[]
a=nn1//2+nn1
for i in range(1,nn1+1):
    if i%2==0:
        lli.append(i)
for i in range(1,nn1+1):
    if i%2!=0:
        lli.append(i)
for i in range(1,nn1+1):
    if i%2==0:
        lli.append(i)
print(a)
print(*lli)
