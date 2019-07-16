aa, bb, ff, kk = map(int, input().split())
count = 0
d = bb-ff
if (d >= 0):
    s = (aa-ff)*2
    for i in range (k):
        if (i == k-1):
             s =s/ 2
        if (d < s):
            d= bb
            count += 1
        d = d - s
        if (d < 0):
            count = -1
            break
        s = 2*aa - s
    print (count)
else:
    print (-1)
