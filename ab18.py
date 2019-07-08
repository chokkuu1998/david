ss,w=map(int,input().split())
Ll=list(map(int,input().split()))
Ll.sort()
Ll.reverse()
oo=w
zz=0
for i in L:
    if(o>=i):
        no=int(o/i)
        z=z+no
        o=o-no*i
    if o==0:
        break
if(o==0):
   print(z)
else:
   print("it's not posiible to select coins ",S)
