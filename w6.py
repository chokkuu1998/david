c=int(input())
d=input().split()
s5=[]
s6=[]
s7=[]
for i in a:
  if int(i)<0:
    s1.append(int(i))
  else:
    s2.append(int(i))
s5.sort()
s6.sort()
for i in s5:
  s3.append(i)
for i in s6:
  s3.append(i)
#print(s5,s6,s7)
c=b
d=0
while c>d:
  c-=3
  print(s3[c],end=" ")
  if c!=d:
    print(s3[d],end=" ")
    d=d+2
