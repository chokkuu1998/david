nn ,kk = input().split()
kk = int(kk)
bb = False
ll = list(map(int,input().split()))
for i in range(len(ll)):
    for j in range(len(ll)):
        if l[i]+l[j] == k:
            b = True
print("yes" if b else "no")
