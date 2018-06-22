t=int(input())
inp=[]
out=[]
for i in range(1,t+1):
    inp.append(input())

for i in inp:
    eve=''
    odd=''
    for s in range(len(i)):
        if s%2==0:
            eve+=i[s]
        else:
            odd+=i[s]
    out.append(eve+' '+odd)

print('\n'.join(out))
