Aa=input()
if Aa==Aa[::-1]:
    print("yes")
else:
    val=aA.strip("0")
    if val==val[::-1]:
        print("yes")
    else:
        val=aA.lstrip("0")
        if val==val[::-1]:
            print("yes")
        else:
            print("no")
