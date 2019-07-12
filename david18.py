ss=input().split()
gg=int(s[1])
mm=int(s[0])
ss=[int(d) for d in s[0]]
hh=0
cc=1;
while(hh==0):
	prod=cc*mm
	k=[ int(d) for d in str(prod)]
	r=0
	j=len(k)-1
	while(k[j]==0):
		r+=1
		j-=1
	if(r>=g):
		print(prod)
		h=1
	c+=1
