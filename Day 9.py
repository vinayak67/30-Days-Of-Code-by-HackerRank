def factorial(num):
    if num==1:
        return 1
    else:
        fact=num*factorial(num-1)
        return fact

n=int(input())
print(factorial(n))
