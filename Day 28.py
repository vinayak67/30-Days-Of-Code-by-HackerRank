
f_name=[]
mail=[]
final_name=[]
if __name__ == '__main__':
    N = int(input())

    for N_itr in range(N):
        firstNameEmailID = input().split()

        firstName = firstNameEmailID[0]

        emailID = firstNameEmailID[1]
        
        
        f_name.append(firstName)
        mail.append(emailID)

for i in range(len(mail)):
    index=mail[i].index('@')
    if mail[i][index:]=='@gmail.com':
        final_name.append(f_name[i])
    

    
final_name=sorted(final_name)
print('\n'.join(final_name))
