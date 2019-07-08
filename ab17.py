ab,by=map(int,input().split())
h=list(map(int,input().split()))
h.sort()
h.reverse()
ab=by
z=0
for i in h:
    if(ab>=i):
        nm=int(ab/i)
        zz=z+nm
        ab=ab-nm*i
    if ab==0:
        break
if(ab==0):
   print(z)
else:
     print("it's not posiible to select coins in such a way that they sum upto",S)  
