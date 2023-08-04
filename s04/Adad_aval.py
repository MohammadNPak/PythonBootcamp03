def is_prime(n):
    if n==1:
        return False
    if n==2:
        return True
    if n%2==0:
        return False
    i = 3
    p = True
    while i<n**0.5+1:
        if n%i==0:
            return False
        i+=2
    return True

a = int(input())
b = int(input())
if a>b:
    a,b=b,a
n=a
while n<=b:
    if is_prime(n):
        print(n)
    n+=1