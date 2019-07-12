kk = int(input())
ll = list(map(int, input().split()))
nn = int(len(l)/2)
if sum(ll[:nn])//len(ll[:nn]) == sum(ll[nn:])//len(ll[nn:]):
    print('yes')
else:
    print('no')
