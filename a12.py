nn,kk = input().split()
nn,kk = int(n),int(k)
Ll1 = [ int(x) for x in input().split()]
Ll2 = [ int(x) for x in input().split()]
max1 = 0
for i in range(0,n) :
    Ll3 = L2[:]
    Ll3[i] += k
    Ll4 = []
    for j in range(0,n) :
        Ll4.append(Ll3[j]//Ll1[j])
    min1 = min(L4)
    if min1 > max1 :
        max1 = min1
print(max1)
