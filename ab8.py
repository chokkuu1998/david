varr,sub=map(int,input().split())
cc=[]
ken=list(map(int,input().split()))
for i in range(0,sub):
    l,h=map(int,input().split())
    cc.append([l,h])
for i in cc:
    d=i[0]-1
    e=i[1]-1
    print(math.gcd(ken[d],ken[e]))
