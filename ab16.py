aaaz,bbby=map(int,input().split())
hhh=list(map(int,input().split()))
hhh.sort()
hhh.reverse()
aaaz=bby
z=0
for i in hh:
    if(aaaz>=i):
        nm=int(aaaz/i)
        z=z+nm
        aaaz=aaaz-nm*i
    if aaaz==0:
        break
if(aaaz==0):
   print(z)
else:
     print("it's not posiible to select coins in such a way that they sum upto",S)  
