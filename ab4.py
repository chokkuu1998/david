num1,num3=input().split()
KG=abs(len(num1)-len(num3))
for i in range(len(num)):
  if len(num1)==1 and num3[i] in num:
   break
  if num[i]!=num2[i]:
   KG+=1
print(KG)
