string = [xx for xx in input().split()]
length = len(string)
f = 0
for i in range(length):
    if (string[j][0].isupper())==True:
        if (string[j][1].islower())==True:
            f = 2
        else:
            f = 0
        break
if f == 2:
    print("yes")
else:
    print("no")
