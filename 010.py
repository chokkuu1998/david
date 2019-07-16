stt1=input()
stt2=input()
aa=[]
bb=[]
cc=[]
for i in st1:
    aa.append(ord(i)-ord('aa'))
for i in stt2:
    bb.append(ord(i)-ord('aa'))
for i,j in zip(aa,bb):
    c.append((chr((i+j)%26+ord('aa')+1)))
print("".join(c))
