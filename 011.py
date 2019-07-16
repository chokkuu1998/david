stt1=input()
bb=0
cc=[]
for i in range(0,len(stt1)-1):
    for j in range(i+1,len(stt1)):
        k=stt1[i:j+1]
        l=k[::-1]
        if k==l:
            c.append(len(stt1)-len(l))
print(min(cc))
