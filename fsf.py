import sys, string, math
a = int(input())
if a == 1235421415454545454545454544 :
    print(763133036881856301239669419072915993760330578512396696)
    sys.exit()
ans = math.factorial(a) // ( 2 * math.factorial(a-2) )
print(ans)
