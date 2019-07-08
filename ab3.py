(num, xx) =input().split()
xx=int(xx)
arr=[]
comb=combinations(num,len(num)-xx)
comb=list(comb)
#print(comb)
for i in (comb):
    arr.append("".join(i))
#print(arr)
print(min(arr))
