ooo, aaa, fff, kkk = map(int, input().split())
count = 0
aa2 = aa-ff
if (aa2 >= 0):
    di = (oo-ff)*2
    for i in range (kk):
        if (i == kk-1):
             di =di/ 2
        if (aa2 < di):
            aa2 = aa
            count += 1
        aa2 = aa2 - di
        if (aa2 < 0):
            count = -1
            break
        di = 2*oo - di

    print (count)
else:
    print (-1)
