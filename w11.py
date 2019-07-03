nn=int(input())
l=[]
for i in range(0,nn):
	for j in range(i,nn):
		l.append("1")
	print(*l)
	l=[]
