import sys, string, math

a = input()
if a == a[::-1] :
    print('yes')
    sys.exit()
k = 0
for c in a[::-1] :
    if c == '0' :
        k += 1
    else :
        break
a2 = '0'*k + a
#print(a2)
if a2 == a2[::-1] :
    print('yes')
else :
    print('no')

