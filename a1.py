ss=input()
l=list(ss)
l1=[]
s12=""
for i in l:
	if l.count(i)==1:
		l1.append(i)
s2=s2.join(l1)
print(s2)
