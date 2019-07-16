inpp=input()
dumm=[]
for i in inp:
  if i not in dumm:
    dumm.append(i)
  else:
    break  
print(len(dumm))
