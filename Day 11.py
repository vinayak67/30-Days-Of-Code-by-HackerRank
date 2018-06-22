arr=[]
temp=[]

for i in range(6):
    k=input()
    temp=list(map(int,k.split(' ')))
    len_temp=len(temp)
    if len_temp<6:
        for y in range(len_temp,6):
            temp.append(0)
    arr.append(temp)


fin_sum=0
for i in range(len(arr)-2):
    for j in range(len(arr[i])-2):
        temp_sum=arr[i][j]+arr[i][j+1]+arr[i][j+2]+arr[i+1][j+1]+arr[i+2][j]+arr[i+2][j+1]+arr[i+2][j+2]
        
        if(i==0 and j==0):
            fin_sum=temp_sum
        if fin_sum<temp_sum:
            fin_sum=temp_sum
        else:
            pass
        temp_sum=0

print(fin_sum)
            
