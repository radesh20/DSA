r=int(input("enter the range: "))
print("prime numbers between 1 to",r,"are:")
num=0


for i in range(2,r+1):
    is_prime=True

    for num in range(2,i):
        if(i%num==0):
            is_prime=False
            break
    if is_prime:
        print(i)
