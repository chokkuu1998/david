zz, yy, xx, ww = map(int, input().split())
cc = 0
aa =yy-xx
if (aa >= 0):
    d = (zz-xx)*2
    for i in range (ww):
        if (i == ww-1):
             d =d/ 2
        if (aa < d):
            aa = y
            cc += 1
        aa = aa - d
        if (aa < 0):
            count = -1
            break
        d = 2*zz - d

    print (cc)
else:
    print (-1)
