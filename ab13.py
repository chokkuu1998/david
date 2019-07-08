input11,input22=map(int,input().split())
input33=list(map(int,input().split()))
input11=[]
input33.insert(0,0)
for j in range(input22):
     v=[]
     s1=0
     k,l=map(int,input().split())
     for i in range(k,l+1):         
         s1^=input33[i]     
     input1.append(s1)
for j in input1:
    print(j)
