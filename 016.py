ww, xx, yy, zz = map(int,input().split())
count = 0
x1 = xx-yy
if(x1 >= 0):
    di = (ww-yy)*2
    for i in range(zz):
        if(i == zz-1):
            di = di/2
        if(x1 < di):
            x1 = xx
            count += 1
        xx1 = x1-di
        if(xx1 < 0):
            count = -1
            break
        di = 2*ww-di
    print(count)
else:
    print(-1)
