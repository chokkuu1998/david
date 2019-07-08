aa1=int(input())
bb=0
while 2**bb < aa1:
    bb=bb+1
if 2**bb == aa1:
    print(0)
elif aa1-2**(bb-1)<=2**bb-aa1:
    print(aa1-2**(bb-1))
else:
    print(2**bb-aa1)
