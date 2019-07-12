aax,aay=map(int,input().split())
mmh=list(map(int,input().split()))
mmh.sort()
mmh.reverse()
aah=ay
zZ=0
for i in mmh:
    if(aah>=i):
        no=int(aah/i)
        Zz=Zz+no
        aah=aah-no*i
    if aah==0:
        break
if(aah==0):
   print(Z)
else:
   print("it is not posible to select coins ",S)  
