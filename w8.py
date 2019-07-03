m = int(input())
b = list(map(int,input().split()))
for j in range(2,n-3):
  if sum(a[:i]) == sum(a[i+1:]):
    print('yes')
    break
else:
  print('no')
