numbers=12345
sum=0
i=0
while i < numbers:
    temp=numbers%10
    sum=sum+temp
    numbers=numbers//10
print("the sum. is :",sum)