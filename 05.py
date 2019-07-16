nn,kk = input().split()
nn,kk = int(nn),int(kk)
L = [ int(x) for x in input().split()]
#print(nn,kk, L)
for i in range(0,nn) :
    if (86400-L[i]) >= kn :
        print(i+1)
        sys.exit()
    kk -= (86400-L[i])
