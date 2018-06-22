n=int(input())
k=(bin(n)[2:])


count=0
temp=0
for i in k:
    if i=='1':
        temp+=1
        if count-temp==1 or count-temp==-1:
            count=temp
        else: pass
    else:
        temp=0

print(count)
