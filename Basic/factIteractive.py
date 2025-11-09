num=int(input("enter a number: "))
fact=1
i=0
for i in range(1,num+1):
    fact=fact*i
print("the factorial of ",num,"is :",fact)